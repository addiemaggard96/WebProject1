import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

position = soupAPNewsBriefs.find('div', class_='ap-newsbriefitem') #'location of news brief in html')
headline = position.find('a').string
brief = position.find('span', class_= 'topheadlinebody').string #'location of brief in html'
apOffice = brief.split(' (AP) ') [0] #'location of apOffice in html'
fullStory = 'hosted.ap.org' + position.find('a').get('href') #'location of fullStory in html'
ctime = fullStory.split('CTIME=')[1] #'location of ctime in html'

print(headline)
print(brief)
print(apOffice)
print(fullStory)
print(ctime)

#beautiful soup is not working. going to try selenium