from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html',{'title':'О сайте'})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat_id}</p></>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat_slug}</p></>')


def archive(request, year):
    if year > 2023:
        url_redirect = reverse('cats', args=('music', ))
        return redirect(url_redirect)

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{year}</p></>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Не найдено</h1>')
