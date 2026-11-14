from django.shortcuts import render # замість HttpResponse 
import requests


def main_page(request):
    return render(request, 'main.html')

def news(request, extra=None):
    name = request.GET.get('name', 'Олександр')
    return render(request, 'news/news.html', {'name': name})

def management(request, extra=None):
    return render(request, 'management/management.html')

def about(request, extra=None):
    return render(request, 'about/about.html')

def contacts(request, extra=None):
    return render(request, 'contacts/contacts.html')

def about_2020(request):
    return render(request, 'about/about_2020.html')

def about_history(request):
    return render(request, 'about/about_history.html')

def contacts_map(request):
    return render(request, 'contacts/contacts_map.html')

def contacts_us(request):
    return render(request, 'contacts/contacts_us.html')

def management_director(request):
    return render(request, 'management/management_director.html')

def news_yellowsubmarine(request):
    return render(request, 'news/news_yellowsubmarine.html')

def news_2026(request):
    return render(request, 'news/news_2026.html')