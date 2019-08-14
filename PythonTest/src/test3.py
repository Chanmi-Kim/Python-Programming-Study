from selenium import webdriver

browser = webdriver.Chrome('P:\\class\\python\\chromedriver.exe')

# URL 입력 + 이동
browser.get('http://localhost:8088/python/data.do')

print(browser.page_source)

print(browser.find_element_by_css_selector('#name').text)
print(browser.find_element_by_css_selector('#school').text)

browser.find_element_by_css_selector('#btn1').click()
print(browser.find_element_by_css_selector('#email').text)

browser.find_element_by_css_selector('#btn2').click()
print(browser.find_element_by_css_selector('#etc').text)

print(browser.page_source)