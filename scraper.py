import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def scrape_geo_news():
    url = 'https://www.geo.tv/latest-news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='singleBlock')
    return extract_geo_articles(articles)

def scrape_bol_news():
    url = 'https://www.bolnews.com/latest/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='col-lg-6')
    return extract_bol_articles(articles)

def scrape_samaa_news():
    url = 'https://www.samaa.tv/latest-news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='col-12 col-sm-4')
    return extract_samaa_articles(articles)

def extract_geo_articles(articles):
    extracted_articles = []
    for article in articles:
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        image = article.find('img')['data-src']
        date = article.find('span', class_='date').text.strip()
        extracted_articles.append({
            'title': title,
            'link': link,
            'image': image,
            'date': date
        })
    return extracted_articles

def extract_bol_articles(articles):
    extracted_articles = []
    for article in articles:
        title = article.find('h6', class_='title').text.strip()
        link = article.find('a', class_='post-link')['href']
        image = article.find('img')['src']
        date = "Date not available"  # BOL News sample does not provide a date
        extracted_articles.append({
            'title': title,
            'link': link,
            'image': image,
            'date': date
        })
    return extracted_articles

def extract_samaa_articles(articles):
    extracted_articles = []
    for article in articles:
        title = article.find('h3').text.strip()
        link = article.find('a')['href']
        image = article.find('img')['data-src']
        date = article.find('time').text.strip()
        extracted_articles.append({
            'title': title,
            'link': link,
            'image': image,
            'date': date
        })
    return extracted_articles

def scrape_articles():
    client = MongoClient('localhost', 27017)
    db = client['news_db']

    geo_news = scrape_geo_news()
    bol_news = scrape_bol_news()
    samaa_news = scrape_samaa_news()

    db['geo_news'].delete_many({})
    db['bol_news'].delete_many({})
    db['samaa_news'].delete_many({})

    db['geo_news'].insert_many(geo_news)
    db['bol_news'].insert_many(bol_news)
    db['samaa_news'].insert_many(samaa_news)

    print("Articles have been scraped and stored in MongoDB.")