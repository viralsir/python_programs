'''
Write a program to enter the numbers till the user wants
and at the end it should display
the count of positive, negative and zeros entered
'''
op="yes"
count_of_positive=0
count_of_negetive=0
count_of_zero=0
while op=="yes":
    no=int(input("Enter No:"))
    if no>0 :
        count_of_positive =count_of_positive+1
    elif no<0:
        count_of_negetive +=1
    else :
        count_of_zero +=1
    op=input("do you want to continue(yes/no)?:")

print("Count of Positive No:",count_of_positive)
print("Count of Nagetive No:",count_of_negetive)
print("Count of Zero No:",count_of_zero)
