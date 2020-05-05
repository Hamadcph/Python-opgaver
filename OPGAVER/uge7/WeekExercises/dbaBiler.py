import bs4
import requests
from tqdm import tqdm

DbaURL = 'https://www.dba.dk/biler/biler/'


def getSoup(url):
    r = requests.get(
        url,
        headers={
            "User-Agent": "My User Agent 1.0",
            "FROM": "youremail@domain.com",
        },
    )
    r.raise_for_status()

    soup = bs4.BeautifulSoup(r.text, "html.parser")

    return soup


def getCars():
    soup = getSoup(DbaURL)
    divs = soup.findAll(
        'div', {"class": "navigator radioNavigator modulePanel"})
    small = divs[0].findAll("small")
    cars = small[0].text
    print("numbers of cars for sale:", cars)


print(getSoup(DbaURL))
getCars()
