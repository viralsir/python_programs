
  #  FMS : - FILE MANAGEMENT SYSTEM

# name=input("Enter msg:")
# fp=open("first.txt","a")
# fp.write(name)
# fp.close()
#
# fp=open("first.txt","r")
# data=fp.read()
# print(data)
# fp.close()


with open("first.txt", "r") as source:
    with open("second.txt","w") as des:
        des.write(source.read())

print("copy is completed")

