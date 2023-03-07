from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first_app2(request):
    return HttpResponse('<h1>firstapp2 view</h1>')
