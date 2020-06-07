from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.contrib import messages
from itertools import chain
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parser
import pandas as pd
from . models import ScrappedNews, NewsPost, Subscriber, Contact
from . clustering import cluster
from .forms import SubscriberForm, ContactForm
from crawler.newscrawler import crawl_news

TAGS = {'NTC': 1, 'LTE': 2, 'Ncell': 3, 'SmartCell': 1, 'NTA': 2, '5G': 3, 'Huawei': 4,'Samsung': 2,
        'Xiaomi': 1, 'Oppo': 4, 'Vivo': 3, 'Apples':1, 'Laptops': 4, 'Poco': 3}
PAGINATION_NUMBER = 10

def tags():
    tags = TAGS.keys()
    colors = TAGS.values()
    return zip(tags, colors)

def side_news():
    return ScrappedNews.objects.all()[:10]

# Create your views here.
def home(request):
    # Code for newsletter subscription from subscribers. This will write 
    # valid email addresses to our Subscriber model
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.cleaned_data['subscriber']
            try:
                subscriber = Subscriber(subscriber=subscriber)
                subscriber.save()
                messages.success(request, 'Your have successfully subscribed our newsletter. You will be getting most recent updates of our featured news. Thank you !!')
            except:
                messages.error(request, 'Error subscribing newsletter. You have already subscribed !!')
        else:
            messages.error(request, 'Error subscribing newsletter. Please, try again with valid email address !!')    
    
    tech_news = ScrappedNews.objects.filter(category="Tech News")[:4]
    telco_news = ScrappedNews.objects.filter(category="Telco News")[:4]
    gadget_news = ScrappedNews.objects.filter(category="Gadget News")[:4]
    global_news = ScrappedNews.objects.filter(category="Global News")[:4]
    context = {
        'tech_news':tech_news,
        'telco_news':telco_news,
        'gadget_news':gadget_news,
        'global_news':global_news,
        'tags' : tags(),
        'side_news': side_news()
    }
    return render(request, 'technology/home.html', context)

def allNews(request, category):
    if category == 'all':
        all_news = ScrappedNews.objects.all()
    elif category == 'telco':
        all_news = ScrappedNews.objects.filter(category='Telco News')
    elif category == 'gadget':
        all_news = ScrappedNews.objects.filter(category='Gadget News')
    elif category == 'global':
        all_news = ScrappedNews.objects.filter(category='Global News')
    else:
        all_news = ScrappedNews.objects.filter(Q(title__icontains = category) | Q(description__icontains = category) )

    headlines = cluster(all_news)
    news = []
    for h in headlines:
        headlines_cluster = []
        for headline in h:
            headlines_cluster.append(all_news.get(title=headline))
        news.append(headlines_cluster)    
    
    paginator = Paginator(news, PAGINATION_NUMBER)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        news = paginator.page(page)
    except(EmptyPage, InvalidPage):
        news = paginator.page(1)

    index = news.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'category':category,
        'all_news':news,
        'page_range':page_range,
        'tags' : tags(),
        'side_news': side_news()
    }
    return render(request, 'technology/all-news.html', context)

def search(request):
    pass

def searchNews(request):
    news_list = ScrappedNews.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        news_list = news_list.filter(Q(title__icontains = search_query) | Q(description__icontains = search_query))
        paginator = Paginator(news_list, PAGINATION_NUMBER)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            news_list = paginator.page(page)
        except:
            news_list = paginator.page(1)

        index = news_list.number - 1
        max_index = 10
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]

    else:
        news_list = []
        page_range = 1

    context = {
        'news_list':news_list,
        'page_range':page_range,
        'search_query':search_query,
        'tags': tags(),
        'side_news': side_news()
    }
    return render(request, 'technology/searchnews.html', context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']            
            message = form.cleaned_data['message']
            contact = Contact(email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Your message has been sent. Thank you !!')
            return redirect('home')
        else:
            messages.error(request, "Error sending message !")
            return render(request, "home/contact.html", context={"form":form})
    return render(request, 'technology/contact.html', context={"form":form})

def getNews(request):
    crawl_news()
    return render(request, 'technology/getnews.html', context={})
def error_404(request, exception):
    return render(request, 'error_404.html', status='404')

def error_500(request):
    return render(request, 'error_500.html', status='500')
