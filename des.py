# import requests module
import requests
# import BeautifulSoup module
from bs4 import BeautifulSoup
#import pandas as pd
url= ("https://www.jumia.co.ke/mlp-warehouse-clearance-sale/")
response=requests.get(url)
print(response.status_code)
#function to return the content from the url page
def get_content(url):
    soup_content=BeautifulSoup(response.content, "html.parser")
    #soup=soup_content.text
    return soup_content
soup=get_content(url)
#print(soup)
#function to obtain the product names and return a list of product names
def get_productName(soup):
    products=soup.find_all("div", class_="name")
    # returns product names in text
    product_names = [product.text.strip() for product in products]
    return product_names
product_name=(get_productName(soup))
#getting a list of product names
print(product_name)