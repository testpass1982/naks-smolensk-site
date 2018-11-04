from django.shortcuts import render
from .models import Post, Tag, Category, Document

# Create your views here.
def main(request):
    title = "Главная - НАКС Смоленск"
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
    all_news = Post.objects.all()
    all_documents = Document.objects.all()


    content = {
        'title': title,
        'news': all_news,
        'documents': all_documents
    }

    return render(request, 'mainapp/news.html', content)

def contact(request):
    return render(request, 'mainapp/contact.html')