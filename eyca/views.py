from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'eyca/index.html')
    # return HttpResponse("HELLO WORLD")