op=1
rollno=[]
name=[]
maths=[]
sci=[]
eng=[]
while op!=3 :
    print("\t\t Student Info")
    print("\t\t 1.Entry")
    print("\t\t 2.View ")
    print("\t\t 3.Exit ")

    op=int(input("Enter your option :"))

    if op==1:
        op1="yes"
        while op1=="yes":
            rollno.append(int(input("Enter No:")))
            name.append(input("Enter Name :"))
            marks=int(input("Enter Maths Marks:"))
            while not (0<=marks<=100):
                print("invalid marks")
                marks=int(input("Enter Maths Marks:"))
            maths.append(marks)
            marks=int(input("Enter sci Marks:"))
            # checking weather the marks are valid or not
            while not (0<=marks<=100):
                print("invalid marks")
                marks=int(input("Enter Sci Marks:"))
            sci.append(marks)
            marks=int(input("Enter eng Marks:"))
            while not (0<=marks<=100):
                print("invalid marks")
                marks=int(input("Enter eng Marks:"))
            eng.append(marks)
            op1=input("do you want to add another student (yes/no)?:")
    elif op==2:
        for r,n,m,s,e in zip(rollno,name,maths,sci,eng):
            print("Roll NO:",r)
            print("Name :",n)
            print("Maths :",m)
            print("Sci :",s)
            print("Eng :",e)

            if m>33 and s>33 and e>33:
                total=m+s+e
                avg=total/3
                print("total :",total)
                print("Avg:",avg)
                if avg >90:
                    print("Grade : A")
                elif avg>70:
                    print("Grade : B")
                elif avg>55:
                    print("Grade : C")
                else :
                    print("Grade : D")
            else:
                print("you are failed")

    elif op==3:
        print("you are exited ")
    else :
        print("wrong option selected try again !!")



