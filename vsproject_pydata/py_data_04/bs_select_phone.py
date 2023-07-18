import requests
from bs4 import BeautifulSoup

url = 'https://m.blog.naver.com/main6406/222989115231'

# 웹페이지에 HTTP GET 요청
response = requests.get(url)

# 요청에 성공했을 경우
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 휴대폰 인기 순위가 있는 태그 혹은 클래스를 찾아서 추출
    ranking_tags = soup.select('#SE-056caffa-10ae-460a-9227-c2195461cbc1 > div')
    if ranking_tags:
        for tag in ranking_tags:
            print(tag.text)
    else:
        print("휴대폰 인기 순위를 찾을 수 없습니다.")
else:
    print("요청에 실패하였습니다.")
