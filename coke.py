import math
print("amount due : 50 ")
s=50
while s>0:
    a=int(input("insert coin(acceptable coins - 25 cents, 10 cents , 5 cents)  "))
    k=str(a)
    if k=="25" or k=="10" or k=="5":
        s=s-a
        if s>0:
            print("amount due : ",s)
    else:
         print("amount due :",s)

if s<=0:
    print("change owed : ",math.fabs(s))



