import requests
from bs4 import BeautifulSoup
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

    # WORK IN PROGRESS

    # def scrape_walmart(self, url):

    #     URL = url

    #     # options = webdriver.ChromeOptions()
    #     # # options.add_argument("start-maximized")
    #     # options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    #     # chrome_driver_binary = "\home\s14mx\bin\chromedriver"

    #     # driver = webdriver.Chrome(
    #     #     executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.binary_location = '/usr/bin/chromedriver'
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     chrome_options.add_argument('--no-sandbox')
    #     driver = webdriver.Chrome(
    #         executable_path='/usr/bin/chromedriver',
    #         chrome_options=chrome_options)
    #     # driver = webdriver.Chrome(ChromeDriverManager().install())
    #     driver.get(URL)
    #     page = driver.page_source
    #     driver.close()

    #     finds = re.findall(
    #         r'submapType\"\:null},\"currentPrice\"\:{\"price\"\:\d+(?:\.\d+)?', page)

    #     item_found = []

    #     for find in finds:
    #         item_found.append(find)

    #     if item_found is None:
    #         actual_price = "Price not available"
    #         return actual_price
    #     else:
    #         actual_price = re.findall(r'\d+(?:\.\d+)?', item_found[0])
    #         print(float(actual_price[0]))
    #         return (float(actual_price[0]))


if __name__ == "__main__":

    pass
