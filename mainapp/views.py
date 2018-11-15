from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import format_html
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostPhoto, Tag, Category, Document
from .forms import PostForm, ArticleForm, DocumentForm

# Create your views here.
def main(request):
    title = "Главная - НАКС Смоленск"
    docs = Document.objects.filter(publish_on_main_page=True).order_by('-created_date')[:3]
    main_page_news = Post.objects.filter(publish_on_main_page=True).order_by('-published_date')[:3]
    posts = {}
    for post in main_page_news:
        posts[post]=PostPhoto.objects.filter(post__pk=post.pk).first()

    content = {
        'title': title,
        'posts': posts,
        'docs': docs,
    }
    
    return render(request, 'mainapp/index.html', content)

def news(request):
    title = "Новости АЦ"
    all_news = Post.objects.all().order_by('-created_date')
    post_list = [dict({'post': post, 'picture': PostPhoto.objects.filter(post__pk=post.pk).first()}) for post in all_news]
    all_documents = Document.objects.all().order_by('-created_date')[:5]
    paginator = Paginator(post_list, 4) #показываем несколько новостей на странице
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    content = {
        'title': title,
        'news': posts,
        'documents': all_documents
    }

    return render(request, 'mainapp/news.html', content)

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    title = post.title
    attached_images = PostPhoto.objects.filter(post__pk=pk)
    attached_documents = Document.objects.filter(post__pk=pk)
    content = {
        'title': title,
        'post': post,
        'images': attached_images,
        'documents': attached_documents
        # 'post_text': format_html(post.text)
    }

    return render(request, 'mainapp/page_details.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def create_factory(request, content_type):
    print(content_type)
    
    title = f'Create new {content_type}'

    forms = {   
                'post' : PostForm, 
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