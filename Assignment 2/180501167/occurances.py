tstr=input("Enter the string")
freq={}
for i in tstr:
	if i in freq:
		freq[i] +=1
	else:
		freq[i] =1
print("occurances\n"+str(freq))
