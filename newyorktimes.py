#scraping the new york times website
import requests
from bs4 import BeautifulSoup
import csv

url="https://www.nytimes.com/"


response=requests.get(url)
print(response.status_code)
soup=BeautifulSoup(response.content,"html.parser")
#print(soup)
articles=soup.find_all('div', class_="css-hep49k e1yccyp20")
#print(articles)

data={}





for article in articles[:10]:
    titles=article.find("p", class_="indicate-hover").text.strip()
    #print(titles)
    if article.find("p", class_="css-8h5y1w") == None:
        print("no description")
    else:
        descriptions=article.find("p", class_="css-8h5y1w").text.strip()
        print(descriptions)

    
data={'titles': titles, 'descriptions': descriptions}

with open('nytimes.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['titles', 'descriptions'])
    writer.writeheader()
    writer.writerow(data)

  
  




