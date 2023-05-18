from django.shortcuts import render, redirect
from .models import *
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView
# Create your views here.


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsForm

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
