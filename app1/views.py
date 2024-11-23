from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def uma(request):
    return HttpResponse('uma is good women')

def prem(request):
    return HttpResponse('<h1>prem is good boy</h1>')

def hosanna(request):
    return HttpResponse('<h1><marquee>hosanna is good boy</marquee</h1>')

def anshika(request):
    return HttpResponse('<h1>anshika is good girl</h1><i>age is 24</i><b>foddy girl</b>')