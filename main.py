from save import save


def get_urls():
    urls = []
    return urls


if __name__ == "__main__":
    dest = "./dst"
    for url in get_urls():
        save(url=url, dest=dest)
