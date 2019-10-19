amount=int(input("Enter the amount to be robbed by the theif: "))
if amount < 5000 :
    x='Loss'
elif amount > 5000 :
    if amount < 19999 :
        x='Moderate'
elif amount > 20000 :
    x='Good'
print("Profit is {0} ".format(x))
