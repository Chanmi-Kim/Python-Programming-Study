# ex18.py

# 사용자 입력 > insert
import cx_Oracle as oci

conn = oci.connect('hr/java1234@localhost:1522/xe')
cursor = conn.cursor()

name = input('이름 : ')
memo = input('메모 : ')
category = input('카테고리 : ')

sql = "insert into tblMemo values (memo_seq.nextval, :name, :memo, default, :category)"
cursor.execute(sql, name=name, memo=memo, category=category)

conn.commit()
conn.close()

print('쓰기 완료')














