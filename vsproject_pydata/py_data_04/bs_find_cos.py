# requests 모듈을 통해 html 가져와서 bs4로 출력
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

URL = 'https://www.cos.com/'

response = Request(URL, headers={"User-Agent": "Mozilla/5.0"}) # get, post, delete, update
soup=BeautifulSoup(urlopen(response).read(), "html.parser")

# print(html_doc)

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify)
div_tag = soup.find('div', class_='departments')
print(div_tag)

h1 = soup.h1.text
print(h1)
# li_tag = soup.find('li', style='cjs_age_item') # class 는 파이썬에서 class_로 명명
# print(li_tag)