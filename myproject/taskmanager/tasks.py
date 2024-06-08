from celery import shared_task
from .scraper import CoinMarketCapScraper

@shared_task
def scrape_data(coin_acronyms):
    scraper = CoinMarketCapScraper()
    return scraper.scrape(coin_acronyms)
