import cx_Oracle as oci

conn = oci.connect('hr/java1234@localhost:1522/xe')

print(conn.version)

cursor = conn.cursor()

sql = 'select count(*) from tblMemo'
cursor.execute(sql)

print(cursor.fetchone()[0])

sql = 'select * from tblMemo where seq = :seq'
cursor.execute(sql, seq=1)

print(cursor.fetchone())


sql = 'select * from tblMemo'
cursor.execute(sql)

for item in cursor:
    print(item[0], item[1], item[2])



sql = 'select * from tblMemo'
cursor.execute(sql)

for item in cursor:
    print(item[0], item[1], item[2])    
