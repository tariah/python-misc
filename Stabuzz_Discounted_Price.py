import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    find = text.find('>$')
    start_of_price = find + 2
    end_of_price = start_of_price + 4
    return(text[start_of_price:end_of_price])


discount = 0.9
print("The discounted price is: ")
price = get_price()
actual_price = price * discount
print(float(actual_price))


