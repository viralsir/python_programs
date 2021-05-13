'''
list1=[]
for i in range(5):
    list1.append(int(input("Enter No"+ str(i+1)+" :")))


for value in list1:
    if value %2==0:
        print(value)
print("for prime no:")
for value in list1:
    is_prime=True;
    for i in range(2,value):
        if value % i==0:
            is_prime=False
            break;
    if is_prime==True:
        print(value)
'''

# list1=[123,444,[23,44,5],[5],66,45,[2,4,5,6,7,8,9]]
# print(list1[-1][:4])
# list2=[]
# list2.append(int(input("Enter no:")))
# list2.append(int(input("enter no:")))
#
# list1[2][1]=list2
# print(list1)
# print(list2)
# list2.append(56)
# print(list1[2][1][1])
# print(list2)
stuent_list=[[1,"vimal",23,44,55],[2,'vishal',34,55,66]]
title=["Roll no:","Name:","Maths:","Sci:","Eng:"]
for student in stuent_list:
    for t,value in zip(title,student):
        print(t,value)










