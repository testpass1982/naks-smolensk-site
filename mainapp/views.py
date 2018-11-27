from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostPhoto, Tag, Category, Document, Article, Message
from .forms import PostForm, ArticleForm, DocumentForm
from .forms import SendMessageForm, SubscribeForm, AskQuestionForm
from .adapters import MessageModelAdapter
from .message_tracker import MessageTracker
# Create your views here.


def main(request):
    """this is mainpage view with forms handler and adapter to messages"""
    title = "Главная - НАКС Смоленск"
    tracker = MessageTracker()
    if request.method == 'POST':
        request_to_dict = dict(zip(request.POST.keys(), request.POST.values()))
        form_select = {
            'send_message_button': SendMessageForm,
            'subscribe_button': SubscribeForm,
            'ask_question': AskQuestionForm,
        }
        for key in form_select.keys():
            if key in request_to_dict:
                print('got you!', key)
                form_class = form_select[key]
        form = form_class(request_to_dict)
        if form.is_valid():

            # saving form data to messages (need to be cleaned in future)
            adapted_data = MessageModelAdapter(request_to_dict)
            adapted_data.save_to_message()
            print('adapted data saved to database')
            tracker.check_messages()
            tracker.notify_observers()
        else:
            raise ValidationError('form not valid')

    docs = Document.objects.filter(
        publish_on_main_page=True).order_by('-created_date')[:3]

    main_page_news = Post.objects.filter(
        publish_on_main_page=True).order_by('-published_date')[:3]

    posts = {}
    for post in main_page_news:
        posts[post] = PostPhoto.objects.filter(post__pk=post.pk).first()

    main_page_articles = Article.objects.filter(
        publish_on_main_page=True).order_by('-published_date')[:3]

    content = {
        'title': title,
        'posts': posts,
        'docs': docs,
        'articles': main_page_articles,
        'send_message_form': SendMessageForm(),
        'subscribe_form': SubscribeForm(),
        'ask_question_form': AskQuestionForm()
    }

    return render(request, 'mainapp/index.html', content)


def news(request):
    """this is the news view"""
    title = "Новости АЦ"
    all_news = Post.objects.all().order_by('-created_date')
    all_documents = Document.objects.all().order_by('-created_date')[:5]
    post_list = [dict({'post': post, 'picture': PostPhoto.objects.filter(
        post__pk=post.pk).first()}) for post in all_news]
    # показываем несколько новостей на странице
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    articles = Article.objects.all().order_by('-created_date')[:3]

    content = {
        'title': title,
        'news': posts,
        'documents': all_documents,
        'bottom_related': articles
    }

    return render(request, 'mainapp/news.html', content)


def details(request):
    content = request.GET.get('content_type')
    pk = request.GET.get('pk')
    content_select = {
        'post': Post,
        'article': Article
    }
    obj = get_object_or_404(content_select[content], pk=pk)

    common_content = {'title': obj.title}
    if content == 'post':
        attached_images = PostPhoto.objects.filter(post__pk=pk)
        attached_documents = Document.objects.filter(post__pk=pk)
        post_content = {
            'post': obj,
            'images': attached_images,
            'documents': attached_documents,
            'bottom_related': Article.objects.all().order_by(
                '-created_date')[:3]
        }
    if content == 'article':
        tags_pk_list = [tag.pk for tag in obj.tags.all()]
        related_articles = Article.objects.filter(
            tags__in=tags_pk_list).exclude(pk=pk).distinct()
        post_content = {
            'post': obj,
            'related': related_articles,
            'bottom_related': related_articles.order_by('-created_date')[:3]
        }

    context = common_content.copy()
    context.update(post_content)

    return render(request, 'mainapp/page_details.html', context)


def create_factory(request, content_type):

    form_name_select = {
        'post': 'новость',
        'article': 'статью',
        'document': 'документ'
    }
    title = 'Создать {}'.format(form_name_select[content_type])

    forms = {
        'post': PostForm,
        'article': ArticleForm,
        'document': DocumentForm
    }

    if request.method == "POST":

        form_Class = forms[content_type]

        form = form_Class(request.POST)
        if content_type == 'document':
            form = form_Class(request.POST, request.FILES)

        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect('news')
        else:
            messages.error(request, "Error")
            context = {
                'title': 'Исправьте ошибки формы',
                'form': form
            }

            return render(request, 'mainapp/content_edit_form.html', context)
    else:
        form_Class = forms[content_type]
        if content_type in forms:
            context = {
                'title': title,
                'form': form_Class()
            }
        else:
            raise Http404

        return render(request, 'mainapp/content_edit_form.html', context)


def validate_form(request):
    '''view to expand in future with ajax'''
    email = request.GET.get('email', None)
    data = {
        'Email': 'Email success'
    }
    return JsonResponse(data)


def contact(request):
    '''view to contact page - forms will redirect here in future'''
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        context = {
            'name': name,
            'phone': phone
        }
    return render(request, 'mainapp/contact.html', context)


def messages(request):
    '''view to all messages in one page - will be @login_required'''
    # html = '<h1>I\'m working</h1>'
    # return HttpResponse(html)
    messages_list = Message.objects.all()

    context = {
        'messages': messages_list
    }
    return render(request, 'mainapp/messages.html', context)
