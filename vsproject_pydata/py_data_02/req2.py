import requests
from bs4 import BeautifulSoup

url = "https://serieson.naver.com/v3/movie"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
hot_new_movies = soup.find.all("#flicking_paging")

for movie in hot_new_movies:
    img_url = movie.parent.select(".Thumbnail_image_")