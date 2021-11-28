import re
from typing import List

import requests
from bs4 import BeautifulSoup

from article import get_article


def get_urls_from_blog_url(blog_url: str) -> List[str]:
    # TODO: implement here
    assert re.compile("(.*)blog.naver.com/(.*)").match(blog_url)
    r = requests.get(blog_url).text
    soup = BeautifulSoup(r, 'html.parser')
    print(soup)
    links = list(map(lambda x: x.text, soup.find_all('href')))
    print(links)
    view_matcher = re.compile("(.*)blog.naver.com/PostView(.*)")
    urls = list(filter(view_matcher.match, links))
    return urls


def get_urls() -> List[str]:
    urls = ["https://blog.naver.com/guzus/222524175503"]
    return urls


if __name__ == "__main__":
    dest = "dst"
    for url in get_urls():
        get_article(url=url).save_file(dest=dest)
