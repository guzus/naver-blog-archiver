import re

import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, author, title, post):
        self.author = author
        self.title = title
        self.post = post

    def as_markdown(self):
        return f"#{self.title}\n{self.post}"

    def save_file(self, dest):
        markdown = self.as_markdown()
        filename = self.title.replace("/", "-")

        with open(f"{dest}/{filename}.md", "w") as f:
            f.write(markdown)


def get_article(url: str) -> Article:
    url_matcher = re.compile("(.*)blog.naver.com/(.*)/(.*)")
    matches = url_matcher.match(url)
    author = matches.group(2)
    article_id = matches.group(3)
    print(author, article_id)

    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    iframe = soup.find_all('iframe')

    response = requests.get("https://blog.naver.com/" + iframe[0].attrs['src']).text
    iframe_soup = BeautifulSoup(response, 'html.parser')

    return Article(
        author=author,
        title=iframe_soup.find('title').text,
        post=iframe_soup.find('div', attrs={"id": f"post-view{article_id}"})
    )
