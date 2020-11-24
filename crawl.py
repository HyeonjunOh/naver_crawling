from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests


celebrities = ['류준열', '혜리', '이유비', '이동휘']

for i in celebrities:
    baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
    plusUrl = i

    url = baseUrl + quote_plus(plusUrl)
    raw = requests.get(url)
    html = BeautifulSoup(raw.text, 'html.parser')

    profile = html.select("dl.detail_profile")

    span = profile[0].select("dd > span")
    #
    print(span.get_text())
    #
    # birth = span[1].text
    # height = span[2].text
    # weight = span[3].text

    a = profile[0].select('dd > a[href^="https://www.instagram.com/"]')[0].get('href')
    print(a)
