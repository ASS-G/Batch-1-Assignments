def cal(amt):
    if(amt<5000):
       print("loss")
    elif(amt>=5000 and amt<=19999):
       print("profit is moderate")
    elif(amt>=20000):
       print("profit is good")
cal(int(input("enter the amt robbed by the theif:")))
