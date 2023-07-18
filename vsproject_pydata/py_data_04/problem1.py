# 네이트 실시간 이슈 키워드 순위를
# BeautifulSoup를 사용하여 출력하시오

import requests
import time
from bs4 import BeautifulSoup

url = "https://www.nate.com/"


for _ in range(2):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    txt = soup.select(".isKeywordList > li")

    for i in txt:
        rank = i.select_one(".num_rank")
        title = i.select_one(".txt_rank")

        print(rank.text, end=". ")
        print(title.text)
