import requests
import datetime
from bs4 import BeautifulSoup
import json

today = str(datetime.datetime.now().date())

response = []

urlSA = 'http://www.samash.com/electric-string-instruments/'
pageSA = requests.get(urlSA)
soupSA = BeautifulSoup(pageSA.content, 'lxml')

#position = soupSA.find('li', class_='grid-item prod-item')
for position in soupSA.find_all('li', class_='grid-item prod-item'):
    if(position.find('a')):
        itemURL = position.find('a').get('href')
    else:
        itemURL = 'URL not available'
    if (position.find('p', class_='name') and position.find('p', class_='name').b and position.find('p', class_='name').b.a):
        title = position.find('p', class_='name').b.a.string
    else:
        title = 'Title not available'
    # if (position.find('a', class_='description')):
    #    description = position.find('p', class_='price').find('b', class_='sale-price').find('a').string
    # else:
    #    description = 'Description not available'
    if(position.find('p', class_='price') and position.find('p', class_='price').find('b', class_='sale-price')):
        price = (position.find('p', class_='price').find('b', class_='sale-price')).string
    else:
        price = 'Price not available'


# print(itemURL)
# print(title)
# print(price)


    response.append({'Title': title, 'Price': price, 'URL': itemURL})

postingsFile = today + '.SamAsh.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()