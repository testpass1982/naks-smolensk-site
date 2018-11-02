from django.shortcuts import render
from .models import Post, Tag, Category, Document

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

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