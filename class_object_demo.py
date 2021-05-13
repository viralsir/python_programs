'''
OOP : Object Oriented Programming
class : is a bunch of related data.
    or
    is a abstract data type


object : is a unique medimum to access or get data which
are binds together in a ref. class.
    or

object is implementation of a class.

# #create object of student class
# s1=student()
# s2=student()
# s3=s1
# s1.rollno=12
# s1=s2
# s2.rollno=55
# print(s3.rollno)

'''
def is_nagetive(no):
    if no <= 0:
        return True;
    else :
        return False;
class student:
    # member variable


    #constructor or magic method
    def __init__(self,r=0,n="",f=0,c=""):
        self.rollno = r
        self.name = n
        self.fees = f
        self.course = c

    #member defination
    def entry(self):
        self.rollno = int(input("Enter Roll No:"))
        while is_nagetive(self.rollno):
            self.rollno = int(input("Enter Roll No:"))

        self.name = input("Enter Name :")
        self.course = input("Enter Course:")
        self.fees = int(input("Enter Fees :"))
        while is_nagetive(self.fees):
            self.fees = int(input("Enter Fees :"))

    def view(self):
        print("Roll No:", self.rollno)
        print("Name :", self.name)
        print("Course:", self.course)
        print("Fees:", self.fees)

student_list=[]
op1=1
while op1 !=5:
    print("\t\t Student Info ")
    print("\t\t 1.Entry")
    print("\t\t 2.View")
    print("\t\t 3.Search by Rollno")
    print("\t\t 4.Search by Course")
    print("\t\t 5.Exit")

    op1=int(input("Enter Your Option :"))

    if op1==1:
        op="yes"
        while op=="yes":
            s=student()
            s.entry()
            student_list.append(s)
            op=input("do you want to add another student(yes/no)?:")

    elif op1==2:
        for s in student_list:
            s.view()

    elif op1==3:
        rno=int(input("Enter Roll no:"))
        for s in student_list:
            if s.rollno == rno:
                s.view()
                break;

    elif op1==4:
        course = (input("Enter Course:"))
        for s in student_list:
            if s.course == course:
                s.view()


    elif op1==5:
        print("you are exited")
    else :
        print("wrong option selected try again !!")




s2=student(1,"vimal",3434,"c")



