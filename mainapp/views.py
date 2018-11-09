from django.shortcuts import render, get_object_or_404
from django.utils.html import format_html
from .models import Post, PostPhoto, Tag, Category, Document

# Create your views here.
def main(request):
    title = "Главная - НАКС Смоленск"
    # doc_count = len(Document.objects.all())
    main_page_docs = Document.objects.all().order_by('-created_date')[:3]
    main_page_news = Post.objects.all().order_by('-published_date')[:3]
    #articles go here

    content = {
        'title': title,
        'news': main_page_news,
        'docs': main_page_docs
    }
    
    return render(request, 'mainapp/index.html', content)

def news(request):
    title = "Новости АЦ"
    all_news = Post.objects.all().order_by('-created_date')
    all_documents = Document.objects.all()


    content = {
        'title': title,
        'news': all_news,
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