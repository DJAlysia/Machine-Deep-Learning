import requests
from bs4 import BeautifulSoup

url = 'https://nhj12311.tistory.com/520'

# 웹페이지에 HTTP GET 요청
response = requests.get(url)

# 요청에 성공했을 경우
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # h4 태그 중에서 텍스트 추출
    h4_tag = soup.select("h4")
    if h4_tag:
        result = h4_tag[1].text
        print(result)
    else:
        print("해당 태그를 찾을 수 없습니다.")
else:
    print("요청에 실패하였습니다.")