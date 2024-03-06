#scraping from jumia website
import requests
from bs4 import BeautifulSoup


url="https://www.jumia.co.ke/flash-sales/"
response=requests.get(url)
#print(response.status_code)

soup=BeautifulSoup(response.content,"html.parser")
#print(soup.text)
#getting the name of the item
items=soup.find_all('div', class_="info")
print(items)

for item in items:
    #getting the name of the item
    item_name=soup.find('div', class_="name")
    #print(item_name)
    print(item_name.text)
    #finding item price
    item_price=soup.find('div', class_="prc")
    #print(item_price)
    print(item_price.text)
    #finding number of units left
    #item_left=soup.find("div", class_="-pts -df -fw")
    #print(item_left)