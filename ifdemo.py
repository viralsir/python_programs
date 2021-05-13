'''
  if conditon :
    statement (true part)
  else :
    statement (false part)

    relational operator
    operator     symbol
    greater than    >
    less than       <
    equal to        ==
    not equal to    !=
    greater than
    or equal to     >=
    less than or
    equal to        <=

    logical operator
    operator    symbol
    and         and
     or         or
     not        not



'''

no=[]
for i in range(3):
    no.append(int(input("Enter No:")))

is_positive=True
for i in no:
    if i<0:
        is_positive=False;


if is_positive==True:
    if no[0]>no[1] and no[0]>no[2]:
        print(no[0]," is maximum")
    elif no[1]>no[2] and no[1]>no[0]:
        print(no[1]," is maximum")
    else:
        print(no[2]," is maximum")
elif no[0]<0 or no[1]<0 or no[2]<0:
    print(" nagetive no are not allowed  ")
else :
    print(" all no are zero ")





