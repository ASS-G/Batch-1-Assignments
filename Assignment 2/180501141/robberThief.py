amt = int(input("Enter the amount robbed by the thief: "))
if amt < 5000:
  print("Loss")
elif amt < 20000:
  print("Profit is moderate")
else:
  print("Good theft")