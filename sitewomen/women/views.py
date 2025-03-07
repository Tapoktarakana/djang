from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')

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
