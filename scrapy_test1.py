# this code is free for uses under you responsibility, check the politics of the web to scrap
# for any question contact me albanochicharroaltur@gmail.com

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

# ------------------------Change web for the link you'll like to scrapy

web = 'https://www.google.es/search?q=ejercicios+python+resueltos&sxsrf=AOaemvIxPjLGZTdFL2WhOMTtZXPvhFXvIA%3A164322' \
      '2863578&ei=T5fxYZLBIpGQ9u8P24C_6A8&oq=ejercicios+python+resueltos&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQywEyBQgAEMsBMg' \
      'UIABDLATIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgQIIxAnOgUIABCRAjoLCC4QxwEQ' \
      '0QMQkQI6CwguEIAEEMcBEKMCOgUIABCABDoKCC4QxwEQowIQJzoKCC4QxwEQowIQQzoECAAQQzoKCC4QxwEQrwEQQzoLCC4QgAQQxwEQrwE6BQg' \
      'uEIAEOgcIABCABBAKOgcIIxDqAhAnOgUILhCRAjoLCC4QgAQQxwEQ0QM6BggjECcQEzoKCC4QgAQQhwIQFDoKCAAQgAQQhwIQFDoFCC4QywFKBAh' \
      'BGABKBAhGGABQAFiPmwJgga8CaBBwAngAgAHNAogB7zGSAQgwLjM2LjQuM5gBAKABAbABCsABAQ&sclient=gws-wiz'

peticion = Request(web, headers={'User-Agent': 'Mozilla/5.0'})
pagina_web = urlopen(peticion).read()

# ------------------------After the variable soup I recommend you print(soup) for find the label for scrap

with requests.Session() as c:
    soup = BeautifulSoup(pagina_web, 'html5lib')
    for resultados in soup.find_all('div', attrs={'class': 'kCrYT'}):
        print(resultados)