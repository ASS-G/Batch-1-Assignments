val = int
val = int(input("Enter the amount robbed by the thief:"))
if val < 5000:
    print("Loss")
elif val >= 5000 and val <= 19999:
    print("Profit is Moderate")
else:
    print("Good theft")

