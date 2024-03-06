import requests
from bs4 import BeautifulSoup


url=("https://www.nytimes.com/")
response=requests.get(url)
#print(response.content)
#checking if the website is accessible
#print(response.status_code)
soup=BeautifulSoup(response.content, "html.parser")
#print(soup)
#print(soup.prettify())
articles=soup.title.text
print(articles)
 
