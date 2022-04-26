import requests
from bs4 import BeautifulSoup


def titleDownload(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    title = ""
    for title in soup.find_all('title'):
        title = title.get_text().replace(" ", "")

    print(title)
    return title
