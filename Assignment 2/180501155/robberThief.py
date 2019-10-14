val = int(input("enter the amount robbed :"))
if val < 5000:
   print("loss")
elif val >=5000 and val <=19999:
   print("moderate")
else:
   print("good")