def occur(a):
	c=0
	#Array is sorted
	a.sort()
	for i in range(len(a)):
		if a[i]==a[(i+1)%len(a)]:
			c+=1
		else:
			print (a[i] + "->" + str(c+1))
			c=0
s=input("Enter string")
a=[u for u in s]	#Conversion of string to array
print ("Occurances:  ")
occur(a)
