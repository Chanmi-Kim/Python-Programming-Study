# ex14.py

from myrequest import get
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

html = get(url)
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')

print(len(links))

for link in links:
    # "/movie/bi/mi/basic.nhn?code=180374"
    key = '/movie/bi/mi/basic.nhn?code='
    
    if link.get('href') != None and key in link.get('href') and link.get('onclick') == None:
        print(link.get_text())
    













