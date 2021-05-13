from std_lib import *
Passing_Marks=35
subject = ["C", "DBMS", "OOP"]
marks = []

rno = int(input("Enter Roll No:"))
name = input("Enter Name :")
marks=getSubjectList(subject)


print("Roll NO:", rno)
print("Name :", name)
for s, m in zip(subject, marks):
    print(s, m)
if is_Pass(marks):
    print("Pass ")
    grade(avg=sum(marks) / len(marks))

else:
    print("Fail")
