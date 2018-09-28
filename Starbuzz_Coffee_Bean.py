import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    find = text.find('>$')
    start_of_price = find + 2
    end_of_price = start_of_price + 4
    return float((text[start_of_price:end_of_price]))

price_now = input("Do you want price now? ")
if price_now == "Y":
    print(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(900)
        price = get_price()
    print("Buy!")

    
        


