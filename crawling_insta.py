from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

url_list = ['devel5per', 'ryusdb']
baseUrl = "https://www.instagram.com/"
for plusUrl in url_list:
    url = baseUrl + quote_plus(plusUrl)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    insta = soup.select('.v1Nh3.kIKUG._bz0w')

    for i in insta:
        print('https://www.instagram/com' + i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']
        with urlopen(imgUrl) as f:
            if not os.path.isdir('./img/' + plusUrl):
                os.mkdir('./img/' + plusUrl)
            with open('./img/' + plusUrl + '/' + str(len(os.listdir('./img/' + plusUrl + '/')) + 1) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        print(imgUrl)
        print()
    driver.close()
