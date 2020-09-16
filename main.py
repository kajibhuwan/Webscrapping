
import requests
from bs4 import BeautifulSoup
import pandas as pd
baseurl = 'https://www.thewhiskyexchange.com'

productlinks=[]

for x in range(1,2):

    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}#productlist-filter_')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='item')

    productlinks =[]
    for item in productlist:
        for link in item.find_all('a',href=True):
            productlinks.append(baseurl+link['href'])



print(productlinks)

#testlink= 'https://www.thewhiskyexchange.com/p/21446/karuizawa-1984-bot2013-sherry-cask-3663'
whiskylist= []
for link in productlinks:

    r= requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    name= (soup.find('h1', class_='product-main__name' ).text.strip())
    price= soup.find('p',class_='product-action__unit-price').text.strip()
    try:
        rating = soup.find('div', class_='review-overview').text.strip()

    except:
        rating = 'no rating'

    whisky = {
        'name' : name,
        'rating': rating,
        'price': price,
      
    }
    whiskylist.append(whisky)
    print('Saving: ',whisky['name'])
df= pd.DataFrame(whiskylist)
print(df.head(15))



