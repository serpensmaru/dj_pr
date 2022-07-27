from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    print(msg)
    return HttpResponse(msg)


def workdir_view(request):
    directoria = listdir()
    not_list_dir = "<br>".join(directoria)
    return HttpResponse(not_list_dir)
