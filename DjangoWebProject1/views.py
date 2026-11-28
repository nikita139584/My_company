from django.shortcuts import render # замість HttpResponse 
import requests
from form.form import ContactForm

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

def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'form/form.html', {'form': form})

