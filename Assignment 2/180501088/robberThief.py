a=int(input('Enter the amount robbed :'))
s='Profit is '
if a>20000:
	s+='Good'
elif a<5000:
	s+='Loss'
else:
	s+='Moderate'
print(s)