import random
import requests
from bs4 import BeautifulSoup

URL = "http://umuryango.rw/amakuru/"


def get_latest_articles(url):
	''' Getting latest articles from umuryango.rw'''
	
	response = requests.get(url)
	soup =  BeautifulSoup(response.text, 'html.parser')
	LINKS = []
	articles = soup.find_all("div", class_="l8")
	interested_articles = articles[1]
	interested_articles = interested_articles.find_all("div", class_="s4")
	for article in interested_articles:
		link =  article.find('a', href=True)
		LINKS.append(link['href'])

	for link in LINKS:
		print("http://umuryango.rw/"+link)
		print("")
	return LINKS

def main():
	print("Getting started......")
	print("")
	print("GETTING LATEST 10 ARTICLES")
	print("")
	articles = get_latest_articles(URL)

	random_article_to_scrape = random.randint(0, len(articles)-1)
	random_article_to_scrape = articles[random_article_to_scrape]
	
	print("")
	print("Going to Scrape --> ", "http://umuryango.rw/"+random_article_to_scrape)
	print("##################################################################################")

if __name__ == "__main__":
    main()