
op=1
student_list=[]
title=["Roll No","Name:","Maths:","Sci:","Eng:","Phy:"]
while op!=5 :
    print("\t\t Student Info")
    print("\t\t 1.Entry")
    print("\t\t 2.View ")
    print("\t\t 3.Search")
    print("\t\t 4.top 3 in Maths")
    print("\t\t 5.Exit ")

    op=int(input("Enter your option :"))

    if op==1:
        op1="yes"
        while op1=="yes":
            student=[]
            student.append(int(input("Enter No:")))
            student.append(input("Enter Name :"))

            for t in title[2:]:
                marks=int(input("Enter "+ t +"  Marks:"))
                while not (0<=marks<=100):
                    print("invalid marks")
                    marks=int(input("Enter"+ t +" Marks:"))
                student.append(marks)
            student_list.append(student)
            op1=input("do you want to add another student (yes/no)?:")
    elif op==2:
        for student in student_list:
            is_pass=True;
            print(title[0],student[0])
            print(title[1],student[1])
            for t,value in zip(title[2:],student[2:]):
                print(t,value)
                if value<=33:
                    is_pass=False;

            if is_pass==True:
                total=sum(student[2:])
                avg=total/len(student[2:])
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
        else:
            print("no records to display")
    elif op==3:
        s_rollno=int(input("Enter rollno for search:"))
        for student in student_list:
            if s_rollno==student[0]:

                is_pass=True;
                print(title[0],student[0])
                print(title[1],student[1])
                for t,value in zip(title[2:],student[2:]):
                    print(t,value)
                    if value<=33:
                        is_pass=False;

                if is_pass==True:
                    total=sum(student[2:])
                    avg=total/len(student[2:])
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

    elif op==4:
        print("Maths hights marks :")
        maths_highest=[student[2] for student in student_list]
        maths_highest.sort(reverse=True)
        print(maths_highest[:3])

    elif op==5:
        print("you are exited ")
    else :
        print("wrong option selected try again !!")



