from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import format_html
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostPhoto, Tag, Category, Document, Article
from .forms import PostForm, ArticleForm, DocumentForm

# Create your views here.


def main(request):
    title = "Главная - НАКС Смоленск"
    docs = Document.objects.filter(
        publish_on_main_page=True).order_by('-created_date')[:3]
    main_page_news = Post.objects.filter(
        publish_on_main_page=True).order_by('-published_date')[:3]
    posts = {}
    for post in main_page_news:
        posts[post] = PostPhoto.objects.filter(post__pk=post.pk).first()

    main_page_articles = Article.objects.filter(publish_on_main_page=True).order_by('-published_date')[:3]

    content = {
        'title': title,
        'posts': posts,
        'docs': docs,
        'articles': main_page_articles
    }

    return render(request, 'mainapp/index.html', content)


def news(request):
    title = "Новости АЦ"
    all_news = Post.objects.all().order_by('-created_date')
    all_documents = Document.objects.all().order_by('-created_date')[:5]
    post_list = [dict({'post': post, 'picture': PostPhoto.objects.filter(
        post__pk=post.pk).first()}) for post in all_news]
    # показываем несколько новостей на странице
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    content = {
        'title': title,
        'news': posts,
        'documents': all_documents
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
            'documents': attached_documents
            # 'post_text': format_html(post.text)
        }
        # print(post_content)
    if content == 'article':
        tags_pk_list = [tag.pk for tag in obj.tags.all()]
        print(tags_pk_list)
        related_articles = Article.objects.filter(tags__in=tags_pk_list)

        print(related_articles)
        post_content = {
            'post': obj
        }
    
    context = common_content.copy()
    context.update(post_content)        

    return render(request, 'mainapp/page_details.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def create_factory(request, content_type):

    form_name_select = {
        'post': 'новость',
                'article': 'статью',
                'document': 'документ'
    }
    title = f'Создать {form_name_select[content_type]}'

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
