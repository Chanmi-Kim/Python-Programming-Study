# ex22.py
from selenium import webdriver

browser = webdriver.Chrome('P:\\class\\python\\chromedriver.exe')

browser.get('http://lms1.sist.co.kr/worknet/SLogin.asp')

txtid = browser.find_element_by_css_selector("#strLoginID")
txtpwd = browser.find_element_by_css_selector("#strLoginPwd")
btn = browser.find_element_by_css_selector(".login-btn input")

txtid.send_keys('정필립')
txtpwd.send_keys('5154')
btn.click()


# 로딩 딜레이 발생
browser.implicitly_wait(10)

# .popbtmbtn_section > div > a:nth-child(8)
browser.find_element_by_css_selector('.popbtmbtn_section > div > a:nth-child(8)').click()

browser.implicitly_wait(50)

#browser.find_element_by_css_selector('#saveBt').click()

saveBt = browser.find_element_by_css_selector('#saveBt')
browser.execute_script("arguments[0].click();", saveBt)

browser.implicitly_wait(50)

browser.find_element_by_css_selector('input[name=formBD_SUBJECT]').send_keys('질문이 있습니다.')
browser.find_element_by_css_selector('#editor1').send_keys('글 내용입니다.')

# 전송 버튼 . click()















