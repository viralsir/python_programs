'''
Write a program to enter the numbers till the user wants
and at the end it should display
max and min of all.

'''
op="yes"
max=0
min=0
while op=="yes":
    no=int(input("Enter No :"))
    if no>max:
        max=no
    if no<min:
        min=no
    op=input("do you want to Continue(yes/no)?:")

print("max:",max)
print("min :",min)