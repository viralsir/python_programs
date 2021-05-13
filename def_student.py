from std_lib import *

subject=["Maths","Science","English"]
marks=[]

rno=int(input("Enter Roll No:"))
name=input("Enter Name :")
marks=getSubjectList(subject)


print("Roll NO:",rno)
print("Name :",name)
displaysubject(subject,marks)