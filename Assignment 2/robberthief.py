amount=int(input('enter the amount robbed by the thief: '))
if amount<5000:
    print("loss")
elif (amount>=5000) and (amount<=19999):
    print("profit is moderate")
else:
    print("good theft")

