import requests
from bs4 import BeautifulSoup
import re


def get_article(url: str):
    url_matcher = re.compile("(.*)blog.naver.com/(\w+)/(\w+)")
    matches = url_matcher.match(url)
    author = matches.group(2)
    article_id = matches.group(3)
    print(author, article_id)

    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    iframe = soup.find_all('iframe')

    response = requests.get("https://blog.naver.com/" + iframe[0].attrs['src']).text
    iframe_soup = BeautifulSoup(response, 'html.parser')

    article = {
        "author": author,
        "title": iframe_soup.find('title').text,
        "post": iframe_soup.find('div', attrs={"id": f"post-view{article_id}"})
    }
    return article


def convert_to_markdown(article: str):
    markdown = f"#{article['title']}\n{article['post']}"
    return markdown

