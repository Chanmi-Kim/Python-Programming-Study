# ex21.py

'''
Selenium, 셀레니움
- 웹 자동화 테스트 도구
- 사람 + 브라우저 + 서핑 == 프로그램 구현

$ pip install selenium
$ pip list
$ python
>>> import selenium

웹 드라이버(사용중인 브라우저 종류 + 버전)

'''
from selenium import webdriver

# print(type(webdriver))

# 웹 드라이버 호출(= 테스트용 브라우저 실행)
browser = webdriver.Chrome('P:\\class\\python\\chromedriver.exe')

# URL 입력 + 이동
browser.get('http://python.org')

# id-search-field
# submit
# #top .docs-meta a

# 메뉴 중 하나 참조
# docMenu = browser.find_element_by_css_selector("#top .docs-meta a")
# print(type(docMenu))
# docMenu.click()


# 검색어 입력 + 버튼 클릭
txt = browser.find_element_by_css_selector("#id-search-field")
txt.send_keys('module')

submit = browser.find_element_by_css_selector("#submit")
submit.click()




















