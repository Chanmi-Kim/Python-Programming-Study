# ex12.py

from myrequest import get
from bs4 import BeautifulSoup

html = get('http://www.example.com/')

# 소스 분석 + 나누는 작업 > 파싱(Parsing)
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

result = soup.find("h1")
print(type(result))

print(result)
print(result.get_text())










