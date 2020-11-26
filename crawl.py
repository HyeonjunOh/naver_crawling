# from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import re


celebrities = ['류준열', '혜리', '이유비', '이동휘', '이지은', '없는 결과', '김우빈']

for i in celebrities:
    baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
    plusUrl = i

    url = baseUrl + quote_plus(plusUrl)
    raw = requests.get(url)
    html = BeautifulSoup(raw.text, 'html.parser')

    profile = html.select("dl.detail_profile")

    if len(profile) == 1:
        birth = profile[0].find_all(text=re.compile("[0-9]*년 [0-9]*월 [0-9]*일"))
        height = profile[0].find_all(text=re.compile("[0-9]*cm"))
        weight = profile[0].find_all(text=re.compile("[0-9]*kg"))
        print("이름 :", i)
        print("출생 :", birth)
        print("키 :", height)
        print("몸무게 :", weight)

        a = profile[0].select('dd > a[href^="https://www.instagram.com/"]')
        if len(a) == 1:
            print(a[0].get('href'))
    else:
        continue

