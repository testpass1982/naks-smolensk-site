from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import format_html
from django.http import Http404, HttpResponse
from .models import Post, PostPhoto, Tag, Category, Document
from .forms import PostForm, ArticleForm, DocumentForm

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


def create_factory(request, content_type):
    print(content_type)
    
    title = f'Create new {content_type}'

    
    if request.method == "POST":
        forms = {'post' : PostForm(request.POST), 'article': ArticleForm(request.POST), 'document': DocumentForm(request.POST)}
        form = forms[content_type]
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect('news')
    else:
        forms = {'post' : PostForm(), 'article': ArticleForm(), 'document': DocumentForm()}
        if content_type in forms:
            context = {
                'title': title,
                'form': forms[content_type]
            }

        else: 
            raise Http404
        return render(request, 'mainapp/content_edit_form.html', context)