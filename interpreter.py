x=int(input("Enter first number  "))
y=input("Enter operator  ")
z=int(input("Enter second number  "))
print("Expression:",x,y,z,sep="")
if y=="+":
    print(float(x+z))
elif y=="-":
    print(float(x-z))
elif y=="*":
    print(float(x*z))
elif y=="/" and z==0:
    print("division by 0 is not possible :)")
elif y=="/":
    a=x/z
    L=str(a).split(".")
    print(L[0],".",L[1][0],sep="")


