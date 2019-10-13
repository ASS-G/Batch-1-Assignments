amt = int(input("Enter the amount robbed by the thief:"))
if(amt < 5000):
    print("Loss")
elif(amt >= 5000 and amt < 20000):
    print("Moderate")
elif(amt > 20000):
    print("Good")
