# msg='wel come to the world of python'
# msg=list(msg)
# msg.sort()
# print(msg)
# print(msg[::2])
# msg_vo=[c for c in msg if c=='a' or c=='i' or c=='o' or c=='u' or c=='e']
# print(msg_vo)
# vo="aeiou"  # vo=['a','e','u']
# for character in vo:
#     print(character ," :",msg.count(character))


msg="Python is a programming language"
if msg.isupper():
    print("msg is upper case")
elif msg.islower():
    print("msg is lower case")
elif msg.istitle():
    print("msg is title case")
else :
    print("msg is capitalize")


print("upper :",msg.upper())
print("lower :",msg.lower())
print("title:",msg.title())
print("capitalize:",msg.capitalize())
msg="Return@124 R"
for c in msg:
    if c.isalpha():
        print(c," - alphabet")
    elif c.isdigit():
        print(c," - is digit")
    elif c.isspace():
        print(c,"- is space")
    else :
        print(c," is symbol")
msg="Python is a programming language"
msg1=msg.split(" ")
print(len(msg1[0]))

word=input("enter word:")
if word in msg:
    print(word, " in ", msg)
else:
    print(word, " not  in ", msg)

msg="123"
print(msg+"2")

msg="5000"
print(msg.ljust(10,'*'))
print(msg.center(10,'*'))








