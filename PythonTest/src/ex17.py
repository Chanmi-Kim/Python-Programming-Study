# ex17.py

# http://python.org
# - 파이썬 32비트(기본)
# - cxOrcale 모듈(JDBC) - OS - 파이썬 = 비트 동일
'''
1. python x64 설치
2. 이클립스 : 인터프리터 교체
3. pip install requests
    pip install bs4
4. 이클립스 재시작
5. cx_Oracle
  1. $ pip install cx_Oracle
  2. path : 오라클 클라이언트 인스턴스
'''

import cx_Oracle as oci

# 데이터베이스 접속
conn = oci.connect('hr/java1234@localhost:1522/xe')

print(conn.version)

# 반환값이 없는 질의
sql = "insert into tblMemo values (memo_seq.nextval, '홍길동', '메모입니다.', default, '할일')"

# 커서(Statement + ResultSet) 반환
cursor = conn.cursor()

result = cursor.execute(sql)

print(result)

conn.commit()
conn.close()













































