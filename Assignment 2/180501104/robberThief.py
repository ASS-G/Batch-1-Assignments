val=int(input("enter the amount robbed by the thief:"))
print(val)
if val<5000:
   print("loss")
elif val>=5000 and val<=19999:
   print(" profit is Moderate")
elif val>=20000:
   print("profit is good")
 