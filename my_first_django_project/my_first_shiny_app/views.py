import os
from os import listdir

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime



def home_view(request):
    template_name = 'my_first_shiny_app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.isoformat(datetime.now(), sep=' ')
    msg = f'Текущие дата и время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    my_list = listdir(path=os.getcwd())
    msg = f"Список файлов рабочей директории: {my_list}"
    return HttpResponse(msg)