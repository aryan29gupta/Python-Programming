def main():
     a=input("input : ")
     print(twttr(a))


def twttr(a):

    c=""
    for i in a:
        if i not in "aeiou":
            c=c+i
    return f"output : {c}"

if __name__=="__main__":
    main()
