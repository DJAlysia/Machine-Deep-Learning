URL = 'https://www.wikipedia.org/'

# selenium 사용하여
# 한국어메뉴를 클릭해서 이동하시오

driver = webdriver.Chrome()

driver.get(URL)

ko_click = driver.find_element(By.ID, 'js-link-box-ko')

time.sleep(2)
ko_clikc.click()

time.sleep(10)

