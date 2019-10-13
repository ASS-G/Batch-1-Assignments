str=input("enter the string\n")
n=len(str)
a=[]
for i in range(n):
	if str[i] in a:
		i+=1
	else:
		a.append(str[i])
		count=str.count(str[i])
		print(str[i]+"->",count)
		i+=1