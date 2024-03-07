import requests
import csv
import json

url=("https://rickandmortyapi.com/api"+"/character"+"/episode/1,2,3")
response=requests.get(url).json()

print(response)

"""
characters=(response['results'][0:19])
for i in characters:
   print(i['name'])
"""
print(my_book.title)
print(my_book.author)
print(my_book.isbn)
print(my_book.is_checked_out)




"""

#characters=requests.get('https://rickandmortyapi.com/api/character').json()
characters=response.get('characters')
print(characters)
"""
