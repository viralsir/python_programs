# dict1={'billno':1,
#        'cname':'vimal',
#        'product':{1:{'id':1,'name':'mobile','qty':5,'rate':2333},
#                   2:{'id':1,'name':'radio','qty':5,'rate':2333}
#                   }
#        }**********963.//////8521
#
# print(dict1['product'][1]['id'])

billbook={}
billbook['billno']=int(input("enter Bill No:"))
billbook['cname']=input("Enter Customer Name :")
billbook['product']={}
op="yes"
count=1
while op=="yes":
    product={}
    product['id']=int(input("Enter Product Id:"))
    product['Name']=(input("Enter Product Name:"))
    product['Qty']=int(input("Enter Product Qty:"))
    product['Rate']=float(input("Enter Product Rate:"))
    billbook['product'][count]=product
    count=count+1
    op=input("do you want to add another product(yes/no)?:")

print("bill no:",billbook['billno'])
print("Customer Name :",billbook['cname'])
print("id".ljust(10," "),
      "Name".ljust(10," "),
      "qty".ljust(10," "),
      "Rate".ljust(10," "))
for product in billbook['product'].values():

    for value in product.values():
        if type(value)==int or type(value)==float:
            print(str(value).ljust(10," "),end="")
        else:
            print(value.ljust(10," "),end="")
    print("")







