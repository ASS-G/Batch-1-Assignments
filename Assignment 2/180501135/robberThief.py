n = int(input("Enter the amount robbed by the theif:"))
if(n < 5000):
    print("Loss")
elif(n > 5000 and n < 19999):
    print("Profit is Moderate")
else:
    print("Good Theft")
