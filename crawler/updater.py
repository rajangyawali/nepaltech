from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from crawler.newscrawler import crawl_news

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(crawl_news, 'interval', minutes=720)
    scheduler.start()