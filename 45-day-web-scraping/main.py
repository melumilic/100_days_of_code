import json
import requests
from bs4 import BeautifulSoup

response = requests.get("http://news.ycombinator.com?")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tags = soup.find_all(name="a", class_="titlelink")
article_upvote = soup.find_all(name="span", class_="score")
article_texts = []
article_links = []


for article_tag in article_tags:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)

print(article_tags[max_index].getText())
print(article_tags[max_index].get("href"))
print(article_upvotes[max_index])

# to reverse a list you can use [::-1] basically [start:stop:step]
# check robots.txt to figure out what you can and cannot scrape