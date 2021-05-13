pid=int(input("Enter Product Id:"))
pname=input("Enter Product Name :")
pqty=int(input("Enter Product Qty :"))
rate=float(input("Enter Product Rate :"))
discount=float(input("Enter Disocunt(%):"))
tax=float(input("Enter tax(%):"))


print("Product Id:",pid)
print("Product Name :",pname)
print("Product Qty :",pqty)
print("Product Rate :",rate)
price=pqty*rate
print("Product Price:",price)
discount=price*(discount/100)
print("Product Discount :",discount)
tax=price*(tax/100)
print("Product Tax :",tax)
bill_amount=price-discount+tax
print("Bill Amount :",bill_amount)
