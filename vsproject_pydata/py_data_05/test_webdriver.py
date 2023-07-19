import selenium
from selenium import webdriver
import time

# driver_path = 'C:\\KDY\\SET UP\\chromedriver-win64\\chromedriver.exe'

myBrowser = webdriver.Chrome()

# myBrowser.get('https://www.naver.com')
myBrowser.get('https://www.youtube.com')

time.sleep(60)

# def load_driver():
#     driver = webdriver.Chrome()
#     url = "https://www.naver.com"
#     driver.get(url)
    
#     return driver