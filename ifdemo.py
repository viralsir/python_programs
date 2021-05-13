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

no1=int(input("Enter No1:"))
no2=int(input("Enter No2:"))
no3=int(input("Enter No3:"))

if no1>0 and no2>0 and no3>0:
    if no1>no2 and no1>no3:
        print(no1," is maximum")
    elif no2>no3 and no2>no1:
        print(no2," is maximum")
    else:
        print(no3," is maximum")
elif no1<0 or no2<0 or no3<0:
    print(" nagetive no are not allowed  ")
else :
    print(" all no are zero ")





