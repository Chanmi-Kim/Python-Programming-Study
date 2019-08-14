# ex23.py

# 정적 데이터 크롤링
from myrequest import get
from bs4 import BeautifulSoup

# 마우스 오른쪽 버튼 > 페이지 소스 보기
html = get('http://211.63.89.31:8088/python/data.do')
soup = BeautifulSoup(html, 'html.parser')

staticdata = soup.select('.staticdata') # <li> x 4개
print(len(staticdata))

for sdata in staticdata:
    print(sdata.get_text())

print(soup.select('#name')[0].get_text())
print(soup.select('#age')[0].get_text())
print(soup.select('#address')[0].get_text())
print(soup.select('#gender')[0].get_text())

print('-----------------------')

# 동적 데이터 크롤링
dynamicdata = soup.select('.dynamicdata')
print(len(dynamicdata))

for ddata in dynamicdata:
    print('data : ', ddata.get_text())









