a=int(input('Enter the No of Students : '))
k=[]
print('Enter your string : ')
for i in range(a):
	b=input().split('-')
	if b[1] == 'P':
		k.append(b[0])
print('People who were present are : '+str(k))