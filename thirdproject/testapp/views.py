from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1> hello friend good morning</h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1> hello friend good afternoon</h1>')


def good_evening_view(request):
    return HttpResponse('<h1> hello friend good evening</h1>')
