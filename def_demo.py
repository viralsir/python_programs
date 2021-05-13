# def isPositive(no):
#     if no>0:
#         return True;
#     else :
#         return False;
#
# def maximum(no1,no2):
#     if no1>no2:
#         print(no1," is maximum")
#     else:
#         print(no2," is maximum")
#
# def diff(no1,no2):
#     return no1-no2
# print("program start")
#
# n1=int(input("Enter no1:"))
# n2=int(input("Enter No2:"))
# if isPositive(n1)==True and isPositive(n2)==True:
#     maximum(12,33)
#     print(diff(no2=12,no1=33))
# else:
#     print("invalid input")

#default argument
def total(no1=0,no2=0,no3=0):
    return no1+no2+no3

def totallist(list):
    return sum(list)

print(total(12,22,22))
print(total(12,22))
print(total(12))
print(totallist([12,23,3,55,4,5,35]))

print("program end")