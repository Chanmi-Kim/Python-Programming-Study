# ex16.py

from myrequest import get
from bs4 import BeautifulSoup
import urllib
import urllib3
import os

site = 'https://m.comic.naver.com/index.nhn'

#sample = 'http://t1.daumcdn.net/webtoon_episode/m/709baef8f46143399fb1fcacc4c5073b'
sample = 'http://ttcfd.hanatour.com/@cms_300/2014062337/gjdol5/IFC 55층 전망대_1.jpg'

# ('https://image-comic.pstatic.net/mobilewebimg/641253/246', '6c92e168f20860f89af021f1d8b35140_001.jpg')

print(os.path.split(sample))
# sampleName = os.path.split(sample)[1]

# print(sampleName)

# 파일 저장(다운로드)
urllib.request.urlretrieve(urllib.parse.quote(sample.encode('utf8'), '/:'), 'webtoon/test.png')
# print('저장 완료')


'''
url = 'http://211.63.89.31:8088/spring/list.action'
html = get(url)
soup = BeautifulSoup(html, 'html.parser')
'''


# selector = 'head > meta'
# meta = soup.select(selector)
# print(meta)


'''
selector = '#list > div > img'
images = soup.select(selector)

# print(len(images))
site = 'http://211.63.89.31:8088'
title = '웹툰'
n = 1

for image in images:
    # print(image)
    urllib.request.urlretrieve(site + image.get('src'), 'webtoon/' + title + str(n) + '.png')
    n =  n + 1
    print(str(n) , '다운로드 완료')
    
print('완료')    
    



'''



















