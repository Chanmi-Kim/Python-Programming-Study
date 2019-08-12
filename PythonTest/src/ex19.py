# ex19.py
import cx_Oracle as oci

conn = oci.connect('hr/java1234@localhost:1522/xe')
cursor = conn.cursor()

# 단일값
sql = 'select count(*) from tblMemo'
# result = cursor.execute(sql)
# print(result)
cursor.execute(sql)

result = cursor.fetchone(); # rs.next() -> rs.getXXX()
print(result[0])


# 단일값&다중값 -> DTO 반환
sql = 'select * from tblMemo where seq = :seq'

cursor.execute(sql, seq=2)

result = cursor.fetchone();
print(result)
print(result[0])
print(result[1])
print(result[2])


sql = 'select * from tblMemo order by seq'
cursor.execute(sql)

print(type(cursor)) # 집합으로써 루프 탐색 지원

for row in cursor:
    # print(row) # 레코드 1줄
    print(row[0])
    print(row[2])


cursor.execute(sql)
for row in cursor:
    # print(row) # 레코드 1줄
    print(row[0])
    print(row[2])












