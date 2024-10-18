l=["January","February","March","April","May","June","July","August","September","October","November","December"]
b=0
L=[]
K=[]
a=input("Date:  ")
if "/" in a:
    L=a.split("/")
    if len(L)==3:
        if len(L[2])==4 and L[2].isdigit():
            print(L[2],"-",end="",sep="")


        if L[0].isdigit():
            if 1<=int(L[0])<=12:
                if int(L[0])<=9:
                    print("0",L[0],"-",end="",sep="")
                else:
                    print(L[0],"-",end="",sep="")


        if L[1].isdigit():
            if L[0] in "13578" or int(L[0])==10 or int(L[0])==12:
                if 1<=int(L[1])<=9:
                    print("0",L[1],end="",sep="")
                elif 9<int(L[1])<=31:
                    print(L[1],end="",sep="")
            elif L[0] in "469" or int(L[0])==11:
                if 1<=int(L[1])<=9:
                    print("0",L[1],end="",sep="")
                elif 9<int(L[1])<=30:
                    print(L[1],end="",sep="")
            elif int(L[0])==2:
                if int(L[2])%4==0:
                    if 1<=int(L[1])<=9:
                        print("0",L[1],end="",sep="")
                    elif 10<=int(L[1])<30:
                        print(L[1],end="",sep="")
                else:
                    if 1<=int(L[1])<=9:
                        print("0",L[1],end="",sep="")
                    elif 10<=int(L[1])<=28:
                        print(L[1],end="",sep="")




else:
    K=a.split()
    if len(K[2])==4 and K[2].isdigit():
        print(K[2],"-",end="",sep="")


    if K[0].isalpha():
        if K[0].capitalize() in l:
            c=l.index(K[0])
            b=c+1
            if 1<=b<=9:
                print("0",b,"-",end="",sep="")
            elif 9<b<=12:
                print(b,"-",end="",sep="")


    if len(K[1])==2 or len(K[1])==3:
        n=K[1].split(",")
        if str(b) in "13578" or b==10 or b==12:
            if 1<=int(n[0])<=9:
                print("0",n[0],end="",sep="")
            elif 10<=int(n[0])<=31:
                print(n[0],end="",sep="")
        elif str(b) in "469" or b==11:
            if 1<=int(n[0])<=9:
                print("0",n[0],end="",sep="")
            elif 9<int(n[0])<=30:
                print(n[0],end="",sep="")
        elif b==2:
            if int(K[2])%4==0:
                if 1<=int(n[0])<=9:
                    print("0",n[0],end="",sep="")
                elif 9<int(n[0])<=29:
                    print(n[0],end="",sep="")
            else:
                if 1<=int(n[0])<=9:
                    print("0",n[0],end="",sep="")
                elif 9<int(n[0])<=28:
                    print(n[0],end="",sep="")

print()
print() 
