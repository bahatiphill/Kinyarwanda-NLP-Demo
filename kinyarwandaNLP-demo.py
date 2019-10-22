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


def scrape_single_article(link):
	response = requests.get(link)
	soup = BeautifulSoup(response.text, 'html.parser')

	article_body = soup.find_all("div", class_="wrapart")[1]
	
	paragraphs =  article_body.find_all('p')
	paragraphs =  [paragraph.text for paragraph in paragraphs]
	print("")
	print("PRINT Paragraphs from the Article")
	print('**********************************')
	for par in paragraphs:
		print(par)
		print("")
	return paragraphs



def main():
	print("Getting started......")
	print("")
	print("GETTING LATEST 10 ARTICLES")
	print("")
	articles = get_latest_articles(URL)

	random_article_to_scrape = random.randint(0, len(articles)-1)
	random_article_to_scrape = articles[random_article_to_scrape]
	random_article_to_scrape = "http://umuryango.rw/"+random_article_to_scrape
	
	print("")
	print("Going to Scrape --> ", random_article_to_scrape)
	print("##################################################################################")
	scrape_single_article(random_article_to_scrape)

if __name__ == "__main__":
    main()