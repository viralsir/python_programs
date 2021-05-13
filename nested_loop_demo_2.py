start=int(input("enter no:"))
end=int(input("Enter No"))

while start<end:
    n = start
    i = 1
    while i <= 10:
        print(n, " * ", i, "=", n * i)
        i += 1
    print("========")
    start+=1


