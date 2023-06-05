from django.shortcuts import render


def index(request):
    return render(request, 'myblog/index.html')

def article(request):
    return render(request, 'myblog/article.html')
