#  If elif program
amount=int(input("Enter the amount robbed by the thief:"))
if amount<5000:
	print("Loss")
elif amount>5000 and amount<19999:
	print("Profit is Moderate")
else:
	print("Good Theft")

