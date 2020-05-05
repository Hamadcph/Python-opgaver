from bs4 import BeautifulSoup as soup
import requests
from urllib.request import urlopen as UReq

# spørgsmål 1: Webscrape alle titlerne på artiklerne som vises på denne side og print dem alle samt antallet af dem

my_url = 'https://www.dr.dk/nyheder/tema/coronavirus'

uClient = UReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
# print(page_soup.title)

# grabs each product
containers = page_soup.findAll("span", {"class": "dre-teaser-title__text"})
# print(containers)

print(len(containers))

for container in containers:
    title_container = container.findAll("span", "dre-compact-teaser__title")
    article_name = title_container[0].text

print(article_name)
