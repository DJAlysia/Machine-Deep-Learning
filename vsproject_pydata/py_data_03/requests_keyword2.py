import re
import requests

URL = 'https://serieson.naver.com/v3/movie'
response=requests.get(URL)
html_data=''
if response.status_code == 200:
    print('접속성공')
    html_data = response.text
# print(html_data)

start = html_data.find('<h2 class="HomeAside_title__b_GC3">')
print(start)
end = html_data.find('<ul class="TopRanking_top_ranking_list__3IHOs">')
print(end)

html_movie = html_data[start:end]
# print(html_subject)

# 방법(MY)
# pattern = r'<h2 class="HomeAside_title__b_GC3">([^<]+)<'
# match = re.search(pattern, html_movie)
# if match:
#     text = match.group(1)
#     print(text)


pattern1 = '<h2.*/h2>'
mat = re.search(pattern1, html_movie)
h2_subject = mat.group()
print(h2_subject)
pattern2 = '<.+?>'
subject_temp = re.sub(pattern2, '', h2_subject)
print(subject_temp)
subject = subject_temp[0:subject_temp.find('더보기')]
print(subject)
