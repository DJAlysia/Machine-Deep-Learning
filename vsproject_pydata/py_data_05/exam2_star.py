import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By # 4버전 이후 태그정보
# from selenium.webdriver.common.keys import Keys
import time # 디버깅 -> 실제는 wait 함수
import random # 일시정지시간을 랜덤하게 변경
from bs4 import BeautifulSoup
sleep_time = random.uniform(0.5, 2.0) # 0.5 ~ 2.0 사이에 랜덤값 (예)0,5555445

driver = webdriver.Chrome()
URL = 'https://www.starbucks.co.kr/index.do'
driver.get(URL)

time.sleep(2)
gnb_store = driver.find_element(By.CSS_SELECTOR, 'a.this')
gnb_store.click()
                                                                              
time.sleep(10)