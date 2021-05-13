'''
Write a program to
add first seven terms
of the following series using a for loop:

'''
no=2
n=int(input("enter no:"))
ans=1
while no<=n:

    if no%2==0:
        ans -= 1/no
    else :
        ans += 1/no
    no+=1

print("ans :",ans)