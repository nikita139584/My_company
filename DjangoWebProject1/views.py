from django.shortcuts import render # замість HttpResponse 
import requests


def main_page(request):
    return render(request, 'main.html')

def news(request, extra=None):
    return render(request, 'news/news.html', {
        'extra' : extra 
        })

def management(request, extra=None):
    return render(request, 'management/management.html', {
        'extra': extra
    })

def about(request, extra=None):
    return render(request, 'about/about.html')


def contacts(request, extra=None):
    return render(request, 'contacts/contacts.html', {
        'extra': extra
    })



