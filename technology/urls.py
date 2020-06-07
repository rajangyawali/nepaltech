from django.urls import path
from . import views

app_name = 'technology'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<str:category>/', views.allNews, name='news'),
    path('search/', views.searchNews, name = 'searchnews'),
    path('contact/', views.contact, name='contact'),
    path('get-news/', views.getNews, name='get-news')
]
