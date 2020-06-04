from technology.models import ScrappedNews
from itertools import chain
from dateutil.parser import parser
from technology.news import (prabidhi_technews, prabidhi_gadgetnews, ktmpost_technews, gadgetbyte_technews, 
                    techlekh_technews, nepalitelecom_technews, nepalitelecom_telconews, nepalitelecom_gadgetnews,
                    techsathi_technews, techsathi_gadgetnews)

def crawl_news():        
    technews = prabidhi_technews()
    for data in technews.itertuples():
        try:
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Prabidhi News', category='Tech News')
        except:
            print('Error fetching Tech News from Prabidhi')

    gadgetnews = prabidhi_gadgetnews()
    for data in gadgetnews.itertuples():
        try:        
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Prabidhi News', category='Gadget News')
        except:
            print('Error fetching Gadget News from Prabidhi')

    technews = ktmpost_technews()
    for data in technews.itertuples():
        try:
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], category='Global News')
        except:
            print('Error fetching Global News from Kathmandu Post')

    technews = gadgetbyte_technews()
    for data in technews.itertuples():
        try:            
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6], category='Tech News')
        except:
            print('Error fetching Tech News from Gadgetbyte')

    technews = techlekh_technews()
    for data in technews.itertuples():
        try:        
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6], category='Tech News')
        except:
            print('Error fetching Tech News from Techlekh')

    technews = nepalitelecom_technews()
    for data in technews.itertuples():
        try:
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6], category='Tech News')
        except:
            print('Error fetching Tech News from Nepali Telecom')

    telconews = nepalitelecom_telconews()
    for data in telconews.itertuples():
        try:        
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6], category='Telco News')
        except:
            print('Error fetching Telecom News from Nepali Telecom')

    gadgetnews = nepalitelecom_gadgetnews()
    for data in gadgetnews.itertuples():
        try:            
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = data[5], posted = data[6], category='Gadget News')
        except:
            print('Error fetching Gadget News from Nepali Telecom')

    technews = techsathi_technews()
    for data in technews.itertuples():
        try:
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Tech Sathi', posted = data[6], category='Tech News')
        except:
            print('Error fetching Tech News from Tech Sathi ')

    gadgetnews = techsathi_gadgetnews()
    for data in gadgetnews.itertuples():
        try:            
            ScrappedNews.objects.create(title=data[1],description=data[2], url = data[3],image_url = data[4], author = 'Tech Sathi', posted = data[6], category='Gadget News')
        except:
            print('Error fetching Gadget News from Tech Sathi')

