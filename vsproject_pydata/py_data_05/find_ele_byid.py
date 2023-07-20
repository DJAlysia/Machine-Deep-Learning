import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = 'https://shoemuf.com/'

webdriver.get(URL)

ele_btn = webdriver.find_element(By.ID, 'postBtn')
print(ele_btn.tag_name)
print(ele_btn.text)
time.sleep(10)
