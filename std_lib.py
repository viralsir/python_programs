Passing_Marks=33

def checkmarks(subject):
    mark=int(input("Enter "+subject+" marks:"))
    while not (0<=mark<=100):
        mark=int(input("Enter "+subject+"marks:"))
    return mark

def is_Pass(marks):
    for m in marks:
        if m<Passing_Marks:
            return False;
    return True;


def getSubjectList(subject):
    marks=[]
    for s in subject:
        marks.append(checkmarks(s))
    return marks

def grade(avg):
    if avg>90:
        print("Grade :A")
    elif avg>70:
        print("Grade : B")
    else :
        print("Grade : C")

def displaysubject(subject,marks):
    for s, m in zip(subject, marks):
        print(s, m)
    if is_Pass(marks):
        print("Pass ")
        grade(avg=sum(marks) / len(marks))

    else:
        print("Fail")
