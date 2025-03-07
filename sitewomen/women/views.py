from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
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
