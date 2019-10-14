def cal(amt):
    if(amt < 5000):
        print("Loss")
    elif(amt >= 5000 and amt <= 19999):
        print("Profit is Moderate")
    elif(amt >= 20000):
        print("Profit is Good")

cal(int(input("Enter the amount robbed by the theif: ")))
