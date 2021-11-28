import requests
from bs4 import BeautifulSoup


def get_article(url: str = "https://blog.naver.com/guzus/222545736588"):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    iframe = soup.find_all('iframe')
    response = requests.get("https://blog.naver.com/" + iframe[0].attrs['src']).text
    iframe_soup = BeautifulSoup(response)
    table = iframe_soup.find('table', attrs={"id": "printPost1"})
    print(table)
    return table


def convert_to_markdown(body: str):
    return ""
