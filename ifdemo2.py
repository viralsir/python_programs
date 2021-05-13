no=1
end=int(input("enter no of records:"))
while no<=end:

    rollno=int(input("Enter No:"))
    name=input("Enter Name :")
    maths=int(input("Enter Maths Marks:"))
    while not (0<=maths<=100):
        print("invalid marks")
        maths=int(input("Enter Maths Marks:"))
    sci=int(input("Enter sci Marks:"))
    # checking weather the marks are valid or not
    while not (0<=sci<=100):
        print("invalid marks")
        sci=int(input("Enter Sci Marks:"))
    eng=int(input("Enter eng Marks:"))
    while not (0<=eng<=100):
        print("invalid marks")
        eng=int(input("Enter eng Marks:"))


    print("Roll NO:",rollno)
    print("Name :",name)
    print("Maths :",maths)
    print("Sci :",sci)
    print("Eng :",eng)

    if maths>33 and sci>33 and eng>33:
        total=maths+sci+eng
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
    no+=1


