import cx_Oracle as oci

conn = oci.connect('hr/java1234@localhost:1521/xe')

print(conn.version)

cursor = conn.cursor()

sql = 'insert into tblMemo values (2, :name, :memo, default, :category)'
result = cursor.execute(sql, name='아무개', memo='테스트입니다.', category='할일')
conn.commit()

print(result)

