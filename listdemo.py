list1=[12,235,34,55,636,55,34,155]
# print(list1[-3])
# #slicing
# list2=list1[1:5:2]
# print(list2)
# list1.append(int(input("Enter NO:")))
# print(list1)
# list1[2]=45
# print(list1)
# list1.insert(2,3)
# print(list1)
# list1.insert(7,7)
# print(list1)
print(list1)
#gloable def
print("no of elements :",len(list1))
print("max value :",max(list1))
print("min value :",min(list1))
print("sum of elements :",sum(list1))

# #in built def
# print("count of no:",list1.count(55))
# print("index of ele:",list1.index(34,3))
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# for i in range(list1.count(34)):
#     list1.remove(34)
# print(list1)

#display element
# print(list1)
# print("using while loop ")
# index=0
# while index < len(list1):
#     print(list1[index],end=" ")
#     index +=1
#
# print("\n using for loop ")
# for index in range(len(list1)):
#     print(list1[index],end=" ")
#
# print("\n for each loop ")
#
# for value in list1:
#     print(value,end=" ")
#
# no=int(input("Enter no:"))
# if no in list1:
#     print(no," is in the list")
# else :
#     print(no," is not in the list")

# list1=[1,2,3]
# list2=[]
# list2.append(int(input("Enter no:")))
#
# list3=list1+list2
# print(list1)
# print(list2)
# print(list3)
# print("multplication of ele :",list1*2)

list1=[1,2,3,4]
list2=list1[:]
list1.append(12)
print(list1)
print(list2)
list2.append(45)
print(list1)
print(list2)
list1.extend(list2)
print(list1)
print(list2)
list3=list1.copy()
print(list1)
print(list3)
list3.append(789)
print(list1)
print(list3)

