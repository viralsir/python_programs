# dict1={1:'first','second':2,"third":23.33}
# print(dict1)
# print(dict1['third'])
# dict1['third']=233
# print(dict1['third'])
# dict1['fourth']=int(input("Enter no:"))
# print(dict1)
#
# dict1.__setitem__(input("Enter key :"),input("Enter value :"))
# print(dict1)
# print(dict1.__getitem__('city'))

student={'rollno':1,'name':'vimal','maths':23,'sci':34,'eng':12}

#print only keys
for key in student:
    print(key)
# print only values
for value in student.values():
    print(value)
# # print key and value both
# for key ,value in student.items():
#     print(key,value)
#
# print("no of items :",len(student))
# student.pop('rollno')
# print(student)
name="hello"
print(name[1:])