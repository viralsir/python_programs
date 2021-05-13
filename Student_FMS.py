'''
     Student info being stored into a file
                    created by shivam at 6-4-2021


dbms  : database management system
oracle , mysql ,postgres,sqlserver,---
dr.e.f.code
rdbms  12 rules
    IBM
  seqeal
  sql
python/java/php/ -- sql --- store /read

'''
op="yes"
title=["Roll No","Name","Maths","Sci","Eng"]
while op !=3:
    print("Student Info")
    print("press 1 for Entry")
    print("press 2 for View")
    print("press 3 for Exit ")

    op=int(input("Enter Your option :"))

    if op==1:
        with open("student.txt","a") as file:
            op2="yes"
            while op2=="yes":
                for t in title:
                    file.write(input("enter "+t))
                    file.write("\t")
                file.write("\n")
                op2=input("do you want to Add another record(yes/no)?:")

    elif op==2:
         print("\t view ")
         with open("student.txt","r") as file:
              print(file.read())

    elif op==3:
        print("you are exited")
    else :
        print("wrong option selected try again !!")

