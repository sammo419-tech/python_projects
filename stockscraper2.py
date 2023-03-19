import requests
from bs4 import BeautifulSoup as bs

stocks = input("Ticker Symbol: ")

def getData(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')

    stock = {
        'price' : soup.find('div', {'class' : 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change' : soup.find('div', {'class' : 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
        }
    print(stock)

getData(stocks)



















    



