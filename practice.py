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




"""

#characters=requests.get('https://rickandmortyapi.com/api/character').json()
characters=response.get('characters')
print(characters)
"""
