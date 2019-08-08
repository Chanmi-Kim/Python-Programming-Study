# ex10.py

'''
Prefrences > PyDev > Editor -> 서식 수정 가능

크롤링(Crawing) or 스크래핑(Scraping)
- 웹 상의 원하는(***) 자원(HTML 페이지)을 수집하는 행동 > 가공 > 저장
- 수집하려는 데이터가 있는 장소(비정화된 데이터들) > 일부 원하는 데이터 추출(정형화)

크롤링 과정
1. 원하는 페이지 URL을 정한다.(https://movie.naver.com/)
2. Request을 한다.(페이지 달라고 요구)
3. Response을 통해 페이지 소스를 전달받는다.
4. 페이지 소스를 분석하고 원하는 데이터을 추출한다.
5. 추출된 데이터 > 가공 > 저장

필요한 모듈
- 설치가 필요한 모듈
1. requests
    - request/response 지원하는 작업 제공
    - pip install requests
    
2. Beautiful Soup
    - HTML(XML) > 구문 분석 > 나누는 역할 : 파싱 작업을 해준다.
    - ex) JavaScript DOM과 유사한 방식
    - pip install bs4

파이썬에서 필요한 모듈 설치 방법
- pip 도구 사용
- pip install 패키지명(모듈명)
- pip list
- pip uninstall 패키지명(모듈명)
- >>> import 모듈명
- >>> import requests
- >>> import bs4
'''

import requests

# HTTP GET Request
# http://www.example.com/
url = 'http://www.example.com/'
resp = requests.get(url)

# print(resp.text)

# 응답 헤더 정보
header = resp.headers
print(type(header))
print(header['Server'])
print(header['Date'])

for key in header.keys():
    print('header[%s] = %s' % (key, header[key]))


print(resp.status_code)

# 분석~~~

# 저장
f = open('example.htm', 'w', -1, 'utf-8')
f.write(resp.text)
f.close()
print('저장 완료')
















