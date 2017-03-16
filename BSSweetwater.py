import requests
import datetime
from bs4 import BeautifulSoup
import json

today = str(datetime.datetime.now().date())

response = []

urlSW = 'https://www.sweetwater.com/store/search.php?s=electric+violin&Go=Search'
pageSW = requests.get(urlSW)
soupSW = BeautifulSoup(pageSW.content, 'lxml')

#position = soupSW.find('div', class_='products')
for position in soupSW.find_all('div', class_='product-card'):
    if(position.find('a')):
        itemURL = 'http://sweetwater.com/' + position.find('a').get('href')
    else:
        itemURL = 'URL not available'
    if (position.find('h2', class_='product__name') and position.find('h2', class_='product__name').find('a')):
        title = position.find('h2', class_='product__name').find('a').string
    else:
        title = 'Title not available'
    if (position.find('span', class_='product__description')):
        description = position.find('span', class_='product__description').string
    else:
        description = 'Description not available'
    pricePosition = position.find('em', class_='product__price')
    if(position.find('em', class_='product__price')):
        price = pricePosition.contents[1].contents[1].text.strip()
    else:
        price = 'Price not available'

# print(itemURL)
# print(title)
# print(description)
# print(price)

    response.append({'Title': title, 'Price': price, 'Description': description, 'URL': itemURL})

postingsFile = today + '.Sweetwater.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()


#next, look into organizing order of variables printed
#maybe beak the description up into parts
    #string number
    #violin vs guitar vs ciola vs cello vs mandolin
#try not to include the ads in your final JSON