def main():
    a=input("Enter a greeting : ")
    print(bank(a))



def bank(a):
    L=a.split()
    if L[0][0].lower()=="h" and L[0][0:5].lower()!="hello":
        return f"$20"
    elif L[0][0:5].lower()=="hello":
        return f"$0"
    else:
        return f"$100"



if __name__=="__main__":
    main()


