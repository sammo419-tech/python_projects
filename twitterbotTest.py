import requests
import time

def price():
    url = f"https://api.twelvedata.com/price?symbol=BTC/USD&apikey=API_KEY"
    response = requests.get(url).json()
    response = response['price']
    print(response)



count = 0

while count < 10:
    price()
    time.sleep(3600)
    count = count + 1

#Running on raspberry pi, not on here. This is just a test script





