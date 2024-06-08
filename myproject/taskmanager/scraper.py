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

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class CoinMarketCapScraper:
    #BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape(self, coin_acronyms):
        results = []
        for coin in coin_acronyms:
            self.driver.get(f"https://coinmarketcap.com/{coin.upper()}/")
            time.sleep(5) # Ensure the page loads fully
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
"""
"""
# scraper.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCapScraper:
    def __init__(self):
        self.base_url = "https://coinmarketcap.com/"
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def scrape(self, coin_acronyms):
        results = []
        for coin in coin_acronyms:
            result = self.scrape_coin_data(coin)
            results.append({'coin': coin, 'output': result})
        self.driver.quit()
        return results

    def scrape_coin_data(self, coin_acronym):
        search_url = f"{self.base_url}currencies/{coin_acronym}/"
        self.driver.get(search_url)

        try:
            wait = WebDriverWait(self.driver, 10)

            price = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(@class, "priceValue")]'))).text
            price_change_24h = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "24h %")]/following-sibling::div'))).text
            price_change_7d = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "7d %")]/following-sibling::div'))).text

            return {
                'price': price,
                'priceChangePercentage24h': price_change_24h,
                'priceChangePercentage7d': price_change_7d,
            }
        except Exception as e:
            return {'error': str(e)}


"""

"""
        try:
            data['price'] = self.driver.find_element(By.CLASS_NAME, 'priceValue').text
            data['price_change'] = self.driver.find_element(By.CLASS_NAME, 'sc-15yy2pl-0').text
            data['market_cap'] = self.driver.find_element(By.XPATH, '//div[@class="statsValue"][1]').text
            data['market_cap_rank'] = self.driver.find_element(By.XPATH, '//div[@class="namePillPrimary"]').text
            data['volume'] = self.driver.find_element(By.XPATH, '//div[@class="statsValue"][2]').text
            data['volume_rank'] = self.driver.find_element(By.XPATH, '//div[@class="statsValue"][3]').text
            data['volume_change'] = self.driver.find_element(By.XPATH, '//div[@class="sc-15yy2pl-0"][2]').text
            data['circulating_supply'] = self.driver.find_element(By.XPATH, '//div[@class="statsValue"][4]').text
            data['total_supply'] = self.driver.find_element(By.XPATH, '//div[@class="statsValue"][5]').text
            data['diluted_market_cap'] = self.driver.find_element(By.XPATH, '//div[@class="statsValue"][6]').text
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
        """