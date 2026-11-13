from django.urls import path
from .views import main_page, news, management,about,contacts,news_2026,news_yellowsubmarine,management_director,about_history,about_2020,contacts_us,contacts_map

urlpatterns = [
    path('', main_page, name='main'),

    path('news/', news, name='news'),    
    path('news/2026', news_2026, name='news_2026'),
    path('news/yellowsubmarine', news_yellowsubmarine, name='news_yellowsubmarine'),

    path('management/', management, name='management'),
    path('management/director', management_director, name='management_director'),

    path('about/', about, name='about'),
    path('about/history', about_history, name='about_history'),
    path('about/2020', about_2020, name='about_2020'),

    path('contacts/', contacts, name='contacts'),
    path('contacts/us', contacts_us, name='contacts_us'),
    path('contacts/map', contacts_map, name='contacts_map'),

    path('news/<path:extra>', news, name='news-extra'),
    path('management/<path:extra>', management, name='management-extra'),
    path('about/<path:extra>', about, name='about-extra'),
    path('contacts/<path:extra>', contacts, name='contacts-extra'),


]
