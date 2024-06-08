from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class CoinMarketCapScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run headless if you do not need the browser UI
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape(self, coin_acronyms):
        results = []
        for coin in coin_acronyms:
            self.driver.get(f"https://coinmarketcap.com/currencies/{coin.lower()}/")
            time.sleep(5)  # Ensure the page loads fully
            data = self.extract_data(coin)
            results.append({'coin': coin, 'output': data})
        self.driver.quit()
        return results

    def extract_data(self, coin):
        data = {}
        try:
            data['price'] = self.driver.find_element(By.CSS_SELECTOR, '.priceValue').text
            data['price_change'] = self.driver.find_element(By.CSS_SELECTOR, '.sc-15yy2pl-0.hzgCfk').text
            data['market_cap'] = self.driver.find_element(By.CSS_SELECTOR, '.statsValue:nth-child(1)').text
            data['market_cap_rank'] = self.driver.find_element(By.CSS_SELECTOR, '.namePillPrimary').text
            data['volume'] = self.driver.find_element(By.CSS_SELECTOR, '.statsValue:nth-child(2)').text
            data['volume_rank'] = self.driver.find_element(By.CSS_SELECTOR, '.statsValue:nth-child(2)').text
            data['volume_change'] = self.driver.find_element(By.CSS_SELECTOR, '.sc-15yy2pl-0.hzgCfk').text
            data['circulating_supply'] = self.driver.find_element(By.CSS_SELECTOR, '.statsValue:nth-child(3)').text
            data['total_supply'] = self.driver.find_element(By.CSS_SELECTOR, '.statsValue:nth-child(4)').text
            data['diluted_market_cap'] = self.driver.find_element(By.CSS_SELECTOR, '.statsValue:nth-child(5)').text
            data['contracts'] = [
                {
                    "name": "solana",
                    "address": self.driver.find_element(By.XPATH, '//div[text()="solana"]/following-sibling::div').text
                }
            ]
            data['official_links'] = [
                {
                    "name": "website",
                    "link": self.driver.find_element(By.XPATH, '//a[text()="Website"]').get_attribute('href')
                }
            ]
            data['socials'] = [
                {
                    "name": "twitter",
                    "url": self.driver.find_element(By.XPATH, '//a[text()="Twitter"]').get_attribute('href')
                },
                {
                    "name": "telegram",
                    "url": self.driver.find_element(By.XPATH, '//a[text()="Telegram"]').get_attribute('href')
                }
            ]
        except Exception as e:
            data['error'] = str(e)
        return data

