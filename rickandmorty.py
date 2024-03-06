import requests
import csv
import json

url=("https://rickandmortyapi.com/api/character")



#fetching data from the API
def get_data(url):
    response=requests.get(url)
    print(response.status_code)
    #an if to handle errors
    if response.status_code==200:
        #print(response.json()['characters']
        #ata=json.loads(response.text)
        data=(response.json()['results'])
        #print(data)
        for i in data:
            #getting character names for first 20 characters
            character=(i['name'])
            print(character)
            #getting location for first 20 locations 
            location=(i['location']['name'])
            print(location)
            #getting episode for first 20 episodes
            episodes=(i['episode'])
            print(episodes)
            
    
    else:
        print(f"Error: {response.status_code}")
    
    
rickmorty=get_data(url)

with open('rickandmorty.csv', 'w')as csv_writer:
    csvwriter=csv.writer(csv_writer, delimeter='\t')
    for line in csv_writer:
        csv_writer.writerows(rickmorty)
        
    
    





    



  








