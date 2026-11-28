from django.urls import path
from . import views
from .views import main_page, news, management,about,contacts,form

urlpatterns = [
    path('', main_page, name='main'),

    path('news/', views.news, name='news'),    

    path('management/', views.management, name='management'),
   
    path('about/', about, name='about'),


    path('contacts/', views.contacts, name='contacts'),

    path('form/', views.form, name='form'),

    path('news/<path:extra>', views.news, name='news-extra'),
    path('management/<path:extra>', views.management, name='management-extra'),
    path('contacts/<path:extra>', views.contacts, name='contacts-extra'),
    path('contacts/<path:extra>', contacts, name='contacts-extra'),


]
