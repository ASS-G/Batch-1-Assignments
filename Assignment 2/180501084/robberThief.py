amt=int(input("enter the amount robbed by the thief"))
if amt<5000:
	print("Loss")
elif amt>5000 and amt<20000:
	print("Profit is moderate")
elif amt==20000:
	print("Profit is good")
