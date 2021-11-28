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

    @staticmethod
    def get_article_from_url(url: str):
        url_matcher = re.compile("(.*)blog.naver.com/(.*)/(.*)")
        matches = url_matcher.match(url)
        author = matches.group(2)
        article_id = matches.group(3)

        response = requests.get(f"https://blog.naver.com/PostView.naver?blogId={author}&logNo={article_id}").text
        iframe_soup = BeautifulSoup(response, 'html.parser')

        return Article(
            author=author,
            title=iframe_soup.find('title').text,
            post=iframe_soup.find('div', attrs={"id": f"post-view{article_id}"})
        )
