
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv



url= ("https://www.jumia.co.ke/mlp-warehouse-clearance-sale/")


response=requests.get(url)
#function to return the content from the url page
def get_content(url):
    soup_content=BeautifulSoup(response.content, "html.parser")
    #soup=soup_content.text
    return soup_content

soup=get_content(url)



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

"""
#function to get the product brand name
def get_productBrandname(soup):
    product_names = [product.text.strip() for product in products]
    for i in product_names:
        Brandname=product_name.split()
"""

    



#function to return the products prices
def get_productPrice(soup):
    prices=soup.find_all("div", class_="prc")
    #iterating over the product list to get a list of each item
    product_prices=[price.text.strip() for price in prices]
    return product_prices

product_price=get_productPrice(soup)
print(product_price)


#function to return the discount on the products
def get_discount(soup):
    discounts=soup.find_all("div", class_="bdg _dsct")
    #iterating over the discounts list to get the corrosponding discounts of the products
    products_discount=[discount.text.strip() for discount in discounts]
    return products_discount

product_discount=get_discount(soup)
print(product_discount)



#def get_totalReviews(soup):
    
#function to get the product's rating out of five
def get_productRating(soup): 
    ratings=soup.find_all('div', class_="stars _s")
    total_rating=[rating.text.strip() for rating in ratings]
    return total_rating

product_rating=get_productRating(soup)
print(product_rating)


#list of list with the products
productlist=[product_name,product_price,product_discount,product_rating]

#df=pd.DataFrame(


#writing the data product data into a csv file
with open('product.csv','w') as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerows(productlist)

   












        
