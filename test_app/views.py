from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sayHi(request):
    print('sayhi')
    return HttpResponse({'final project \n \tGhaith - Zaher - Riad - AbdElwahap'})
