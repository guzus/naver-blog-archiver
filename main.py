import argparse
import json
import re
from typing import List

import requests

from article import Article


def get_urls_from_blog_url(blog_url: str) -> List[str]:
    author = re.compile("(.*)blog.naver.com/(.*)").match(blog_url).group(2)
    curr_page, count_per_page, total_count = 1, 5, None
    article_urls = []
    while total_count is None or curr_page * count_per_page <= total_count:
        url = f"https://blog.naver.com/PostTitleListAsync.naver?blogId={author}&currentPage={curr_page}&countPerPage={count_per_page}"
        response = requests.get(url).text.replace('\\', '\\\\')
        data = json.loads(response)
        posts = data.get("postList")
        total_count = int(data.get("totalCount"))
        for post in posts:
            log_no = post.get("logNo")
            article_url = f"https://blog.naver.com/PostView.naver?blogId={author}&logNo={log_no}"
            article_urls.append(article_url)
        curr_page += 1
    return article_urls


def get_urls() -> List[str]:
    return ["https://blog.naver.com/guzus/222524175503"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='options')
    parser.add_argument('--url', help='url of a blog article')
    parser.add_argument('--blog', help='url of a blog')
    parser.add_argument('--dest', help='destination directory where blog article should be saved')
    args = parser.parse_args()

    dest = args.dest or "dst"
    urls = [args.url] or get_urls()
    blog = args.blog

    if blog:
        for url in get_urls_from_blog_url(blog):
            Article.get_article_from_url(url=url).save_file(dest=dest)
    else:
        for url in urls:
            Article.get_article_from_simple_url(url=url).save_file(dest=dest)
