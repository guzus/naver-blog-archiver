import argparse
import re
from typing import List

import requests

from article import Article


def get_urls_from_blog_url(blog_url: str) -> List[str]:
    # TODO: implement here
    author = re.compile("(.*)blog.naver.com/(.*)").match(blog_url).group(2)
    print(author)
    # API for getting article ids
    # https://blog.naver.com/PostTitleListAsync.naver?blogId=guzus&viewdate=&currentPage=1&categoryNo=&parentCategoryNo=&countPerPage=5
    curr_page = 1
    count_per_page = 10
    # while
    r = requests.get(
        f"https://blog.naver.com/PostTitleListAsync.naver?blogId={author}currentPage={curr_page}&countPerPage={count_per_page}").json
    print(r)
    # r.postList : list of post
    # r.totalCount : count of post
    urls = []
    # url should be : https://blog.naver.com/PostView.naver?blogId={author}&logNo={logNo}
    print(urls)
    return urls


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
            Article.get_article_from_url(url=url).save_file(dest=dest)
