import psycopg2

#make connection
conn=psycopg2.connect(host="localhost",
                      dbname="afternoon_db",
                      user="postgres",
                      password="1234")
#make a cursor(buffer)
cur=conn.cursor()
op1=1
while op1 !=4 :
    print("\t\t Student Info ")
    print(" press 1 for Entry ")
    print(" press 2 for View ")
    print(" press 3 for Search")
    print(" press 4 for Exit ")

    op1=int(input("Enter your option :"))

    if op1 == 1:
        op2="yes"
        while op2.lower() =="yes":
            rno=int(input("Enter Roll no:"))
            name=input("Enter Name :")
            maths=int(input("Enter Maths Marks:"))
            sci=int(input("Enter Sci Marks:"))
            eng=int(input("Enter Eng Marks:"))
            cur.execute("insert into student values(%s,%s,%s,%s,%s)",(rno,name,maths,sci,eng))
            conn.commit()
            op2=input("Do you want to add another student(yes/no)?:")
    elif op1==2:
        print("\t view ")
        cur.execute("select rollno,sname,maths,sci,eng,maths+sci+eng, case(maths>35 and sci>35 and eng>35) when true then 'pass' else 'fail' end from student ")
        for row in cur:
            for value in row:
                print(value,end="\t")
            print("")
    elif op1==3:
        rid=int(input("Enter Roll No:"))
        print("\t view ")
        cur.execute(
            "select rollno,sname,maths,sci,eng,maths+sci+eng, case(maths>35 and sci>35 and eng>35) when true then 'pass' else 'fail' end from student  where rollno=%s",(rid,))
        for row in cur:
            for value in row:
                print(value, end="\t")
            print("")

    elif op1==4:
        print("you are exited ")
    else :
        print("wrong option selected ")

cur.close()
conn.close()