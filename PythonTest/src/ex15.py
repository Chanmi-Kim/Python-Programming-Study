# ex15.py
# http://weather.naver.com

# import requests
from myrequest import get # 페이지 소스 긁어오기
from bs4 import BeautifulSoup # 소스 분석하기

url = 'https://weather.naver.com/period/weeklyFcast.nhn'

html = get(url)

# print(html)

soup = BeautifulSoup(html, 'html.parser')

# 탐색 방법 1 - 태그 단일 요소 검색
h5 = soup.find('h5')
print(h5)

h6 = soup.find('h6')
print(h6)

strong = soup.find('strong')
print(strong)

dd = soup.find('dd')
print(dd)

td = soup.find('td')
print(td)


# 탐색 방법 2 - 태그 다중 요소
tds = soup.find_all('td')
print(len(tds))

# for td in tds:
#     print(td) 
    
    
images = soup.find_all('img')

key = 'https://ssl.pstatic.net/static/weather/images/w_'

for image in images:
    if key in image.get('src'):
        print(image.get('title'))    



# 탐색 방법 3 - CSS 선택자 지원
images = soup.select('.tbl_wk tbody td img')

print(len(images))

for image in images:
    print(image.get('title'))


kweather = soup.select('#banner_kw > a > img')
print(kweather)















