import requests

# URL = 'https://www.burgerking.co.kr/#/'
URL2 = 'https://serieson.naver.com/v3/movie/search' # 네이버 영화

param = {'query':'스페셜'}
response = requests.get(URL2, params=param) # 웹 사이트 주소에 요청
# print('응답코드:', response.status_code)
if response.status_code==200:
    print('성공')
else



