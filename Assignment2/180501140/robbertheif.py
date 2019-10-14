amount=int(input("Enter the amount robbed by the thief:"))
if amount<5000:
  print("\nComplete loss for the theif")
elif amount>=5000 and amount<=19999:
  print("\nProfit is moderate!")
elif amount>20000:
  print("\nGood theft for the theif!!")

