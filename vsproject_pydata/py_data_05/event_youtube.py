# URL = 'https://www.youtube.com/'

# 검색어: 이순신

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By # ver3 -> 4 update
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # 앞으로 이렇게만 기억함

URL = 'https://www.youtube.com/'
driver.implicitly_wait(10) # 암묵적으로 계속 10초 지연

driver.get(URL)

time.sleep(2)
# cdx-text-input__input
# input_search = driverfind_element(By.NAME, 'search')
input_search = driver.find_element( By.CLASS_NAME,'style-scope ytd-searchbox' )
# input_search = driver.find_element( By.CSS_SELECTOR,'cdx-text-input__input' )

time.sleep(2)
input_search.click()
input_search.send_keys('이순신')

# time.sleep(2)
# cdx-search-input__end-button
# btn_search = driver.find_element(By.CLASS_NAME, 'cdx-search-input__end-button')

# time.sleep(2)
# btn_search.click()
input_search.send_keys(Keys.ENTER)

time.sleep(10)

