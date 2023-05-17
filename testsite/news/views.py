from django.shortcuts import render, redirect
from .models import *
from .forms import NewsForm
# Create your views here.

def news_home(request):
    data2 = News.objects.all()
    data = {
        'title': 'Новости',
        'news': data2
    }

    return render(request, 'news/news_home.html', data)

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'
    form = NewsForm()
    data = {
        'title': 'Создание статьи',
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
