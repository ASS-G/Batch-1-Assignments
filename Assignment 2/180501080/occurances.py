a=input('Enter a string : ')
k=[]
m=0
b=list(set(a))
b.sort()
#print(b)
for j in range(len(b)):
	for i in a:
		if b[j]==i :
			m+=1
	k.append(m)
	m=0
for i in range(len(k)):
	print(str(b[i])+'->'+str(k[i]))