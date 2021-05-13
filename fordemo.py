start=int(input("enter no:"))
end=int(input("Enter No"))
for j in range(start,end+1):
    for i in range(1,11):
        print(j,"*",i,"=",j*i)
    print("=============")
