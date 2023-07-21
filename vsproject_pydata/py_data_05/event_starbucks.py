# URL = 'https://www.starbucks.co.kr/store/store_map.do'


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By # ver3 -> 4 update
from selenium.webdriver.common.keys import Keys
import time
import random

sleep_time = random.uniform(0.5, 1.1)
driver = webdriver.Chrome() 

URL = 'https://www.starbucks.co.kr/store/store_map.do'
driver.implicitly_wait(10) 

driver.get(URL)

time.sleep(sleep_time)
input_search = driver.find_element( By.ID,'quickSearchText' )

time.sleep(sleep_time)
input_search.click()
input_search.send_keys('타임스퀘어2')

time.sleep(sleep_time)
btn_search = driver.find_element(By.CLASS_NAME, 'quickSearchBtn')

time.sleep(sleep_time)
btn_search.click()

time.sleep(sleep_time)
btn_click = driver.find_element(By.CLASS_NAME, 'pin_general')
btn_click.click()


time.sleep(10)