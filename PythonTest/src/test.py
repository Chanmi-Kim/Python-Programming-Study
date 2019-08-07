import cx_Oracle as oci

conn = oci.connect('hr/java1234@localhost:1521/xe')

print(conn.version)