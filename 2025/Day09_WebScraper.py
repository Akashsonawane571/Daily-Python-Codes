# Day09_WebScraper.py
# Simple Web Scraper using requests + BeautifulSoup

import requests
from bs4 import BeautifulSoup

def scrape_quotes(url="http://quotes.toscrape.com/"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise error for bad response
    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for quote, author in zip(quotes, authors):
        quotes_data.append({"quote": quote.text, "author": author.text})

    return quotes_data


if __name__ == "__main__":
    print(" Scraping quotes...")
    quotes_list = scrape_quotes()

    for i, q in enumerate(quotes_list[:5], start=1):  # show first 5 quotes
        print(f"\n{i}. \"{q['quote']}\" — {q['author']}")
