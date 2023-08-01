import requests
from bs4 import BeautifulSoup

req = requests.get("https://gamer33.ru/shop/gejmpad-ps5-dualsense-edge-belyj-chernyj/")

soup = BeautifulSoup(req.content, 'html.parser')

#price = soup.find('div', {'class':'product-buy-modal__total'}).get_text()
price = soup.find('h1', {'class':'product_title entry-title'}).get_text()

print(price)

#<h1 class="product_title entry-title">Геймпад PS5 DualSense Edge (белый/черный)</h1>