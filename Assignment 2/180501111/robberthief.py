def cal(amt):
    if(amt<5000):
        print("Loss")
    elif(amt>=5000 and amt<=19999):
        print("Profit is moderate")
    elif(amt>=20000):
        print("profit is good")

        cal(int(input("enter the amount robbed by thief: ")))
