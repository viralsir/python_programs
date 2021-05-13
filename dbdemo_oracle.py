import cx_Oracle

#initialize the client lib
cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_19_10")
#make a connection
conn=cx_Oracle.connect("system/1234@localhost")
#make a cursor(buffer)
cur=conn.cursor()
#execute query
#cur.execute("create table hr.student_afternoon(rollno number(5),sname varchar(50))")
#cur.execute("insert into hr.student_afternoon values(2,'rajan')")

cur.execute("select * from hr.departments where department_id=20")

for row in cur:
    print(row)

# commit the query
conn.commit()
#print("record is inserted ...")
#close the cursor
cur.close()
#close the connection
conn.close()
