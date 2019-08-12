# ex20.py


from myrequest import get
from bs4 import BeautifulSoup
import os
import urllib
import cx_Oracle as oci
from _operator import sub


# 구현 순서
# 1. 목록 페이지를 접속한다.
# 2. 여행지 링크 주소를 찾는다.
# x 반복
# 3. 2번의 페이지를 접속한다.
# 4. 크롤링 텍스트 or 이미지를 가져온다.
# 5. 4번의 데이터를 데이터베이스에 추가한다.

domain = 'http://info.hanatour.com'
#          http://info.hanatour.com/dest/list/all/1?page=3
total = 'http://info.hanatour.com/dest/list/all/1'
totalHtml = get(total)
totalSoup = BeautifulSoup(totalHtml, 'html.parser')

print(len(totalSoup.select('.listArea a')))


# DB 접속
import cx_Oracle as oci


# cx_Oracle에서 한글 인코딩 처리
os.environ["NLS_LANG"] = ".AL32UTF8"
 
START_VALUE = u"Unicode \u3042 3".encode('utf-8')
END_VALUE = u"Unicode \u3042 6".encode('utf-8')


conn = oci.connect('hr/java1234@localhost:1522/xe')
cursor = conn.cursor()

sql = 'insert into tblHana values (hana_seq.nextval, :title, :subtitle, :place, :time, :address, :tel, :homepage, :pic)'


for item in totalSoup.select('.listArea a'):
    print(item.get('href')) 
    # http://info.hanatour.com/dest/content/all/44?contentID=1000071416101&
    subHTML = get(domain + item.get('href'))
    subSoup = BeautifulSoup(subHTML, 'html.parser')
    
    title = subSoup.select('.nd_spot_d_title')
    if (len(title) != 0):
        # print(title[0].get_text())
        title = title[0].get_text()
    else:
        title = ''
        
    subtitle = subSoup.select('.nd_spot_d_sub_title')
    if (len(subtitle) != 0):
        # print(subtitle[0].get_text())
        subtitle = subtitle[0].get_text()
    else:
        subtitle = ''
        
    place = subSoup.select('.nd_spot_info_wrap > dl > dd:nth-child(2)')
    if (len(place) != 0):
        # print(place[0].get_text())
        place = place[0].get_text()
    else:
        place = ''
        
    time = subSoup.select('.nd_spot_info_wrap > dl > dd:nth-child(4)')
    if (len(time) != 0):
        # print(time[0].get_text())
        time = time[0].get_text()
    else:
        time = ''

    address = subSoup.select('.nd_spot_info_wrap > dl > dd:nth-child(6)')
    if (len(address) != 0):
        # print(address[0].get_text())
        address = address[0].get_text()
    else:
        address = ''

    tel = subSoup.select('.nd_spot_info_wrap > dl > dd:nth-child(8)')
    if (len(tel) != 0):
        # print(tel[0].get_text())
        tel = tel[0].get_text()
    else:
        tel = ''

    homepage = subSoup.select('.nd_spot_info_wrap > dl > dd:nth-child(10)')
    if (len(homepage) != 0):
        # print(homepage[0].get_text())
        homepage = homepage[0].get_text()
    else:
        homepage = ''
        
    pic = subSoup.select('.nd_spot_img_wrap img')
    if (len(pic) != 0):
        # print(pic[0].get('src'))
        pic = pic[0].get('src')
    else:
        pic = ''
    
    # 데이터 수집 완료
    
    print(pic)
    # 사진 다운로드
    # 첨부파일 경로에 한글 들어가서 인코딩 처리
    urllib.request.urlretrieve(urllib.parse.quote(pic.encode('utf8'), '/:'), 'files/' + os.path.basename(pic))
    
    # insert
    cursor.execute(sql, title=title, subtitle=subtitle, place=place, time=time, address=address, tel=tel, homepage=homepage, pic=pic)
    print('추가 완료')

conn.commit()
conn.close()











