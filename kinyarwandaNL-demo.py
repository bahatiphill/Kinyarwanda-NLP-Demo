import requests
from bs4 import BeautifulSoup

URL = "http://umuryango.rw/amakuru/"


def get_latest_article(url):
    #get latest article from umuryango.rw
    response = requests.get(url)
    soup =  BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all("div", class_="l8")
    interested_articles = articles[1]
    interested_articles = interested_articles.find_all("div", class_="s4")
    for article in interested_articles:
        print(article)
        print("")
        print("###########################")
        

def main():
    print("Getting started......")
    get_latest_article(URL)


if __name__ == "__main__":
    main()