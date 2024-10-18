def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
k=[]
l=[]
def is_valid(plate):
    for i in plate:
        l.append(i)
    for j in range(len(l)):
        if 2<=len(l)<=6:
            if plate.isalnum():
                if plate[0:2].isalpha():
                    if plate[j].isdigit():
                        k.append(plate[j])
                        if k[0]=="0":
                            return False
                        if plate[j]!=0:
                            if j<len(l)-1:
                                if plate[j+1].isalpha()=="False":
                                    return True
                        else:
                            return False
                    else:
                        pass
                else:
                    return False
    return plate


main()
