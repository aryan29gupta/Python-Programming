d={}
while True:
    try:
        a=input()
        if a=="":
            break
        elif a not in d :
            d[a]=1
        else:
            d[a]+=1
    except EOFError:
        break

for k,v in d.items():
    print(v,k.upper(),sep=" ")
