from convert import get_article, convert_to_markdown


def save(url: str, dest: str):
    article = get_article(url)
    title = article.get("title").replace("/", "-")
    md = convert_to_markdown(article)

    f = open(f"{dest}/{title}.md", "w")
    f.write(md)
    f.close()
