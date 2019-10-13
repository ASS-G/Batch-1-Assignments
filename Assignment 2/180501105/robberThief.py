s=int(input("Hello robber! How much did you rob?"))
if s<=5000:
    b="Loss"
elif (s>5000 and s<=19999):
    b="Profit is Moderate"
elif s>=20000:
    b="Profit is Good"
print(b)

