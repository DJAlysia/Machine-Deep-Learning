# URL = 'https://datalab.naver.com/'

# 슬라이드 안에 인기분야 순위들 - 맨마지막 영역
# 그 안에 날짜, 순위목록 출력

# import requests
# from bs4 import BeautifulSoup

# URL = 'https://datalab.naver.com/'

# # 웹 페이지의 HTML을 가져옵니다.
# response = requests.get(URL)
# html = response.text

# # BeautifulSoup을 사용하여 HTML을 파싱합니다.
# soup = BeautifulSoup(html, 'html.parser')

# # 슬라이드 안에 있는 영역을 찾습니다.
# slide = soup.find('div', class_='rank_inner v2')

# if slide is not None:
#     # 날짜를 가져옵니다.
#     date_elem = slide.find('strong', class_='rank_title')
#     date = date_elem.text if date_elem else "날짜를 찾을 수 없습니다."
#     print('날짜:', date)

#     # 순위 목록을 가져옵니다.
#     rankings = slide.find_all('ul', class_='rank_list')
#     if rankings:
#         print('순위 목록:')
#         for ranking in rankings:
#             print(ranking.text)
#     else:
#         print('순위 목록을 찾을 수 없습니다.')
# else:
#     print('슬라이드 영역을 찾을 수 없습니다.')

import requests
from bs4 import BeautifulSoup

URL = 'https://datalab.naver.com/'

# 웹 페이지의 HTML을 가져옵니다.
response = requests.get(URL)
html = response.text

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(html, 'html.parser')

# 슬라이드 영역을 찾습니다.
slide = soup.find('div', class_='rank_inner v2')

if slide is not None:
    # 날짜를 가져와 출력합니다.
    date_elems = slide.find_all('strong', class_='rank_title')
    for date_elem in date_elems:
        date = date_elem.text
        print('날짜:', date)

        # 해당 날짜의 순위 목록을 가져와 출력합니다.
        rankings = date_elem.find_next('ul', class_='rank_list')
        if rankings:
            items = rankings.find_all('span', class_='title')
            if items:
                for index, item in enumerate(items, start=1):
                    print(f'{index}. {item.text}')
            else:
                print('순위 목록이 비어있습니다.')
        else:
            print('순위 목록을 찾을 수 없습니다.')
else:
    print('슬라이드 영역을 찾을 수 없습니다.')



import requests
from bs4 import BeautifulSoup

URL = 'https://datalab.naver.com/'

# 웹 페이지의 HTML을 가져옵니다.
response = requests.get(URL)
html = response.text

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(html, 'html.parser')

# 슬라이드 영역을 찾습니다.
slide = soup.find('div', class_='keyword_rank')

if slide is not None:
    # 날짜를 가져와 출력합니다.
    date_elems = slide.find_all('strong', class_='rank_title')
    for date_elem in date_elems:
        date = date_elem.text
        print('날짜:', date)

        # 해당 날짜의 순위 목록을 가져와 출력합니다.
        rankings = date_elem.find_next('ul', class_='rank_list')
        if rankings:
            items = rankings.find_all('span', class_='title')
            if items:
                for index, item in enumerate(items, start=1):
                    print(f'{index}. {item.text}')
            else:
                print('순위 목록이 비어있습니다.')
        else:
            print('순위 목록을 찾을 수 없습니다.')
else:
    print('슬라이드 영역을 찾을 수 없습니다.')



