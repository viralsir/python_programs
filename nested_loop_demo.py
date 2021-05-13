n=int(input("enter No:")) #5->9, 6-> 11, 7-> 13
i=1
m=1
while i<=2*n-1:
    j=n+1
    while j>=1:
        if j>m :
            print(end="  ")
        else:
            print("*",end=" ")
        j-=1
    print("")
    if i<n:
        m+=1
    else:
        m-=1
    i+=1
print("program exit")
'''

'''