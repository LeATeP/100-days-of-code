from bs4 import BeautifulSoup
import requests
import lxml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "0.8",
}

amazon_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B0777XZBMZ/ref=sr_1_1?qid=1597662463&th=1"

response_text = requests.get(amazon_url, headers=headers).text
soup = BeautifulSoup(response_text, "lxml")

w = soup.find("span", {"class": "a-size-medium a-color-price priceBlockBuyingPriceString"})
print(w.string)
















