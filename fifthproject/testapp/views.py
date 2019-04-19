from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_view(request):
    return HttpResponse('<h1> Response from first view </h1>')

def second_view(request):
    return HttpResponse('<h1> Response from second view </h1>')

def third_view(request):
    return HttpResponse('<h1> Response from third_view </h1>')

def fourth_view(request):
    return HttpResponse('<h1> Response from fourth_view view </h1>')

def fifth_view(request):
    return HttpResponse('<h1> Response from fifth_view view </h1>')
