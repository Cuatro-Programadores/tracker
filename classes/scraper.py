import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re


class Scraper:

    def __init__(self, url=None):
        self.url = url

    def scrape_amazon(self, url):

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

        page = requests.get(url, headers=headers)

        soup1 = BeautifulSoup(page.content, "html.parser")

        soup2 = soup1.find_all(class_="a-offscreen")
        if soup2:
            finds = re.findall(
                r'\$\d{1,3}(?:[,]\d{3})*(?:[.]\d{0,2})?|\d{1,3}(?:[ ]\d{3})*(?:[,]\d{0,2})?', str(soup2[0]))

            if finds is None:
                actual_price = "Price not available"
                return actual_price
            else:
                actual_price = re.findall(
                    r'\d{1,3}(?:[,]\d{3})*(?:[.]\d{0,2})?|\d{1,3}(?:[ ]\d{3})*(?:[,]\d{0,2})?', finds[0])
                print(float(actual_price[0]))
                return(float(actual_price[0]))
        else:
            print("999999")
            return 999999

    def scrape_target(self, url):

        URL = url

        page = requests.get(URL)

        soup1 = BeautifulSoup(page.content, "html.parser")

        soup2 = soup1.prettify()

        finds = re.findall(r'current_retail\\\"\:\d+(?:\.\d+)?', soup2)

        item_found = []

        for find in finds:
            item_found.append(find)

        if item_found is None:
            actual_price = "Price not available"
            return actual_price
        else:
            actual_price = re.findall(r'\d+(?:\.\d+)?', item_found[0])
            print(float(actual_price[0]))
            return (float(actual_price[0]))

    def scrape_walmart(self, url):

        URL = url

        # options = webdriver.ChromeOptions()
        # # options.add_argument("start-maximized")
        # options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        # chrome_driver_binary = "\home\s14mx\bin\chromedriver"

        # driver = webdriver.Chrome(
        #     executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = '/usr/bin/chromedriver'
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver',
            chrome_options=chrome_options)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(URL)
        page = driver.page_source
        driver.close()

        finds = re.findall(
            r'submapType\"\:null},\"currentPrice\"\:{\"price\"\:\d+(?:\.\d+)?', page)

        item_found = []

        for find in finds:
            item_found.append(find)

        if item_found is None:
            actual_price = "Price not available"
            return actual_price
        else:
            actual_price = re.findall(r'\d+(?:\.\d+)?', item_found[0])
            print(float(actual_price[0]))
            return (float(actual_price[0]))


if __name__ == "__main__":
    scraper = Scraper()
    # scraper.scrape_amazon(
    #     'https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dp/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1')
    # scraper.scrape_amazon(
    #     'https://www.amazon.com/dp/B07VHZ41L8?ref_=nav_em__k_ods_ha_ta_0_2_4_6')
    # scraper.scrape_amazon(
    #     'https://www.amazon.com/dp/B08F6FYN6B?ref_=nav_em__k_ods_tab_ta_pls_0_2_5_6')
    # scraper.scrape_amazon(
    #     'https://www.amazon.com/gp/product/B0B1352TDK?ie=UTF8&keywords=jewelry&sprefix=je%2Cluxury%2C151&sr=1-1&crid=2KWVNYXW3SHUW&qid=1659393999&ref_=sr_1_1_lx_bd')
    # scraper.scrape_amazon(
    #     'https://www.amazon.com/Natural-Current-NC13KWDYIKIT-Floating-Installation/dp/B00R34C7GG/ref=sr_1_1?crid=2WCGEAFZOK0Z6&keywords=solar+panels&qid=1659395715&sprefix=solar+pa%2Caps%2C148&sr=8-1')
    # scraper.scrape_amazon(
    #     'https://www.amazon.com/Napkins-Lucheon-Beverage-Guest-BIrthday/dp/B00JBG31KK/ref=sr_1_2?crid=258BO8L7ZNNWE&keywords=napkins&qid=1659396596&sprefix=napkins%2Caps%2C186&sr=8-2')

    # scraper.scrape_target(
    #     'https://www.target.com/p/hisense-55-34-class-a6g-series-4k-uhd-android-smart-tv-55a6g/-/A-82802681#lnk=sametab')
    # Scraper.scrape_target(
    #     '``')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/goumikids-thermal-organic-cotton-pants/-/A-85165008?preselect=85165038#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/pompeii3-2ct-huge-diamond-heart-pendant-14k-white-gold/-/A-87091390#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/newair-27-built-in-160-bottle-dual-zone-compressor-wine-fridge-in-stainless-steel-quiet-operation-with-smooth-rolling-shelves/-/A-86737742#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/disposable-paper-napkins-230ct-smartly-8482/-/A-75557241#lnk=sametab')

    scraper.scrape_walmart(
        'https://www.walmart.com/ip/Rayovac-High-Energy-AAA-Batteries-60-Pack-Triple-A-Batteries/45598335')
    # Scraper.scrape_walmart(
    #     'https://www.walmart.com/ip/LG-55-Class-4K-UHD-OLED-Web-OS-Smart-TV-with-Dolby-Vision-A2-Series-OLED55A2PUA/218195189')
    # Scraper.scrape_walmart(
    #     'https://www.walmart.com/ip/Poppy-Women-s-Vegan-Leather-Quilted-Crossbady-Shoulder-Purse-Drawstring-Bucket-Bag-Messenger-Bag/401837777?athbdg=L1900')
    # Scraper.scrape_walmart(
    #     'https://www.walmart.com/ip/Loloi-II-Wynter-WYN-02-Auburn-Multi-Oriental-Area-Rug-8-6-x-11-6/178864229')
    # Scraper.scrape_walmart(
    #     'https://www.walmart.com/ip/Pompeii3-1-1-10ct-Cushion-Halo-Solitaire-Diamond-Engagement-Wedding-Ring-Set-White-Gold/997500370?athbdg=L1700')
    # Scraper.scrape_walmart(
    #     'https://www.walmart.com/ip/Clorox-Toilet-Bowl-Cleaner-with-Bleach-Rain-Clean-24-oz/12443821')
