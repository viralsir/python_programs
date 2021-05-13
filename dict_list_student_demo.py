
op=1
div_student_list={'A':[],"B":[],"C":[]}
#student_list=[]
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
        print("\t\t Entry ")
        op1 = "yes"
        while op1 == "yes":
            for keys in div_student_list.keys():
                print("press ", keys ," for division ",keys)
            div=input("Enter your option :").upper()
            if div not in div_student_list:
                print("invalid option entered ")
            else:
                student={}
                student.__setitem__(title[0],int(input("Enter Roll No:")))
                student.__setitem__(title[1],input("Enter Name :"))

                for t in title[2:]:
                    marks=int(input("Enter "+ t +"  Marks:"))
                    while not (0<=marks<=100):
                        print("invalid marks")
                        marks=int(input("Enter"+ t +" Marks:"))
                    student[t]=marks

                div_student_list[div].append(student)
                op1=input("do you want to add another student (yes/no)?:")
    elif op==2:
        for keys in div_student_list.keys():
            print("press ", keys, " for division ", keys)
        div = input("Enter your option :").upper()
        for student in div_student_list[div]:
            is_pass=True;
            for t,value in student.items() :
                print(t,value)
                if t != title[0] and t!=title[1]:
                    if value<=33:
                        is_pass=False;

            if is_pass==True:
                total=sum(list(student.values())[2:])
                avg=total/len(list(student.values())[2:])
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
        for keys in div_student_list.keys():
            print("press ", keys, " for division ", keys)
        div = input("Enter your option :").upper()

        s_rollno=int(input("Enter rollno for search:"))
        for student in div_student_list[div]:
            if s_rollno==student[0][title[0]]:
                is_pass = True;
                for t, value in student.items():
                    print(t, value)
                    if t != title[0] and t != title[1]:
                        if value <= 33:
                            is_pass = False;

                if is_pass == True:
                    total = sum(list(student.values())[2:])
                    avg = total / len(list(student.values())[2:])
                    print("total :", total)
                    print("Avg:", avg)
                    if avg > 90:
                        print("Grade : A")
                    elif avg > 70:
                        print("Grade : B")
                    elif avg > 55:
                        print("Grade : C")
                    else:
                        print("Grade : D")
                else:
                    print("you are failed")
        else:
            print("no records to display")

    elif op==4:
        pass
        # print("Maths hights marks :")
        # maths_highest=[student[2] for student in student_list]
        # maths_highest.sort(reverse=True)
        # print(maths_highest[:3])

    elif op==5:
        print("you are exited ")
    else :
        print("wrong option selected try again !!")



