from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'eyca/index.html')


def login(request):
    return render(request, 'eyca/login.html')


def register(request):
    return render(request, 'eyca/register.html')