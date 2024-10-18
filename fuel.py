a=input("Fraction  :")
try:
    L=a.split("/")
    b=(int(L[0])/int(L[1]))*100
    if b>=99:
        print("F")
    elif b<=1:
        print("E")
    else:
        print(b,"%")
except ZeroDivisionError:
    pass
except ValueError:
    pass

