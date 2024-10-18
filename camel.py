a=input("CamelCase  :")
print("snake_case  :",end="")
for i in a:
    if i.islower():
        print(i,end="")

    elif i.isupper():
        print("_",end="")
        print(i.lower(),end="")
print()

