import requests
from bs4 import BeautifulSoup as bs
import time

url = 'https://www.google.com/finance/quote/BTC-USD'
r = requests.get(url)
soup = bs(r.text, 'html.parser')

price = soup.find('div', {'class' : 'YMlKec fxKbKc'}).text

count = 0

while count <= 10:
    print(price)
    time.sleep(2)
    count = count + 1