from bs4 import BeautifulSoup as soup
import requests
from urllib.request import urlopen as UReq

# spørgsmål 1: Hvor mange produkter kommer frem, når man søger på "breaking benjamin" (se URL'en)

my_url = 'https://www.merchbar.com/search?q=breaking%20benjamin&p=1'

uClient = UReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
# print(page_soup.title)

# grabs each product
containers = page_soup.findAll("div", {"class": "col-md-4 col-6"})
print(len(containers))
# 20 er svaret
divWithInfo = containers[0].find("div", "MerchTile.module__brandName")
