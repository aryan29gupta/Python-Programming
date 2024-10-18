def convert(a):
    L=a.split()
    for i in L:
        if i==":)":
            print("🙂",end=" ")
        elif i==":(":
            print("🙁",end=" ")
        else:
            print(i,end=" ")

def main():
    a=input("Enter a string")
    convert(a)
main()
