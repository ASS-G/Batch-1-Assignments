a=input('Enter a string : ')
chumma=[]
b=0
x=list(set(a))
x.sort()
for j in range(len(x)):
	for i in a:
		if x[j]==i :
			b+=1
	chumma.append(b)
	b=0
for i in range(len(chumma)):
    print(str(x[i])+'->'+str(chumma[i]))
