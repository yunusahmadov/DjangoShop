from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context={
        'title':'Home - Главная',
        'content': "Магазин мебели HOME"
        }
    # return HttpResponse('Home Page'
    return render(request,'main/index.html',context)

def about(request):
    context={
        'title':'Home - О Нас',
        'content': "О Нас",
        'text_on_page':'Текст о том почему этот магазин лучший'
        }
    # return HttpResponse('Home Page'
    return render(request,'main/about.html',context)