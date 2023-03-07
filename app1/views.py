from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first_app1(request):
    return HttpResponse('<h1>fisrt view of app1</h1>')
def second_app1(request):
    return HttpResponse('second view app1')
