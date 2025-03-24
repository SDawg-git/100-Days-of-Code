from bs4 import BeautifulSoup
import requests

website_url = "https://news.ycombinator.com/news"
response = requests.get(url=website_url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

print(soup)
