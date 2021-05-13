import psycopg2

#make connection
conn=psycopg2.connect(host="localhost",
                      dbname="afternoon_db",
                      user="postgres",
                      password="1234")
#make a cursor(buffer)
cur=conn.cursor()
#execute query
#cur.execute("create table student(rollno int,sname text,maths int,sci int ,eng int)")
# rno=int(input("Enter Roll no:"))
# name=input("Enter Name :")
# maths=int(input("Enter Maths Marks:"))
# sci=int(input("Enter Sci Marks:"))
# eng=int(input("Enter Eng Marks:"))
# cur.execute("insert into student values(%s,%s,%s,%s,%s)",(rno,name,maths,sci,eng))

cur.execute("select * from student")

for row in cur:
    print(row)

# commit the query
conn.commit()
print("record is inserted ...")
#close the cursor
cur.close()
#close the connection
conn.close()
