import requests
from bs4 import BeautifulSoup as bs
import json

stocks = ['AAPL' , 'NVDA', 'AMD', 'GOOG', 'AMZN']
stockdata = []

def getData(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')

    stock = {
        'price' : soup.find('div', {'class' : 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change' : soup.find('div', {'class' : 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
        }
    return stock

for items in stocks:
    stockdata.append(getData(items))
    print("Getting: ", items)

with open('stockdata.json' , 'w') as f:
    json.dump(stockdata, f)

print("Complete")

with open('stockdata.json' , 'r') as file:
    data = json.load(file)

print(f"Close Price: ${data[0]['price']}, Price Change: {data[0]['change']}")
print(f"Close Price: ${data[1]['price']}, Price Change: {data[1]['change']}")
print(f"Close Price: ${data[2]['price']}, Price Change: {data[2]['change']}")
print(f"Close Price: ${data[3]['price']}, Price Change: {data[3]['change']}")
print(f"Close Price: ${data[4]['price']}, Price Change: {data[4]['change']}")
















    



