from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def root(request):  # root url
    return HttpResponseRedirect(reverse('index'))


def index(request):  # root url
    return render(request, 'index.html')


def demo(request):
    return render(request, 'demo.html')


def article(request):
    return render(request, 'article.html')


def message(request):
    return render(request, 'message.html')


def diary(request):
    return render(request, 'diary.html')