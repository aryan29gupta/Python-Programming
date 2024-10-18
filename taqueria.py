sum=0
while True:
    key=input("Item  :")
    if key=="":
        break
    d={"Baja Taco": 4.25,"Burrito": 7.50,"Bowl": 8.50,"Nachos": 11.00,"Quesadilla": 8.50,"Super Burrito": 8.50,"Super Quesadilla": 9.50,"Taco": 3.00,"Tortilla Salad": 8.00}
    for i in d:
        if key.lower()==i.lower():
            sum+=d[i]
            print("Total  :$",sum)
        else:
            pass



