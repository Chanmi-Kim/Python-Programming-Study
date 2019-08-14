# ex24.py

# 동적 데이터 크롤링(JavaScript로 발생하는 데이터)
from selenium import webdriver
# from bs4 import BeautifulSoup

browser = webdriver.Chrome('P:\\class\\python\\chromedriver.exe')
browser.get('http://211.63.89.31:8088/python/data.do')

# print(browser.page_source)
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup.select('#school')[0].get_text())

# print(browser.find_element_by_css_selector('#school').text)


# 정적 데이터
# browser.find_elements_by_class_name('staticdata')
staticdata = browser.find_elements_by_css_selector('.staticdata')
print(len(staticdata))

for sdata in staticdata:
    print(sdata.text)

print(browser.find_element_by_css_selector('#name').text)
print(browser.find_element_by_css_selector('#age').text)
print(browser.find_element_by_css_selector('#address').text)
print(browser.find_element_by_css_selector('#gender').text)

print('----------------------')

# 동적 데이터 크롤링
print(browser.find_element_by_css_selector('#school').text)

# 버튼 클릭
# print(browser.page_source)
browser.find_element_by_css_selector('#btn1').click()
# print(browser.page_source)
print(browser.find_element_by_css_selector('#email').text)


browser.find_element_by_css_selector('#btn2').click()
print(browser.find_element_by_css_selector('#etc').text)

# browser.close()























