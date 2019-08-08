# ex13.py
from myrequest import get
from bs4 import BeautifulSoup

html = get('http://naver.com')
soup = BeautifulSoup(html, 'html.parser')

result = soup.find_all('a')
print(type(result))

print(len(result))

for link in result:
    print(link.get_text(), '-', link.get('href'))
    
    












