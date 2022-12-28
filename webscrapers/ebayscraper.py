import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.ebay.com/itm/175551484729?hash=item28dfaf1339%3Ag%3Ap5wAAOSw7MJjq6RQ&amdata=enc%3AAQAHAAAAoJQjjI1m0Bap5DGWgMSgUEK%2Bx1pFRDQnfgA%2Ftjo%2BUX%2BeAQtLENGRztCpJQgQnuT0PPwjjoMAXypw8AkWiuw0DwSj3f%2BFYPOLPIhGPMqwlGOk%2FPjF8Q0cLEO8XImuatsXCnGR1vSHObYtAF%2BhxAFr%2FgmFnesqyL2weYNczMAUIQwLkP5VQdT11LCxRHrdEaXiXrlnVYgIHJY3Rf%2Bgvc3FJDI%3D%7Ctkp%3ABk9SR-DWwPiqYQ&LH_Auction=1'
r = requests.get(url)
soup = bs(r.text, 'html.parser')

current_price = soup.find('div', {'class': 'x-price-primary'}).text
number_of_bids = soup.find('div', {'class': 'x-bid-count'}).text

print(f"Current bid: {current_price}")
print(f"Bids: {number_of_bids}")