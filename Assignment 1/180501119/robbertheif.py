

def cal(amt):

   if(amt<5000):
     print("loss")
   elif(amt>= 5000 and amt<= 1999):
     print("profit is moderate")
   elif(amt>=20000):
     print("profit is good")

cal(int(input("Enter the amount robbed by the theif:")))
