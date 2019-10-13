amount=int(input("Enter the amount robbed by the thief:"))
if amount<5000:
  print("\nComplete loss")
elif amount>=5000 and amount<=19999:
  print("\nModerate profit!")
elif amount>20000:
  print("\nGood theft amount!!")