from save import save


def get_urls_from_id(id: str):
    pass


def get_urls():
    urls = ["https://blog.naver.com/guzus/222524175503"]
    return urls


if __name__ == "__main__":
    dest = "dst"
    for url in get_urls():
        save(url=url, dest=dest)
