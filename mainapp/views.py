from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def news(request):
    return render(request, 'mainapp/news.html')

def contact(request):
    return render(request, 'mainapp/contact.html')