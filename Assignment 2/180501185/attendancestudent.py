a=int(input('Enter the No of Students : '))
b=[]
print('Enter your string : ')
for i in range(a):
	b=input().split('-')
	if b[1] == 'P':
		k.append(b[0])
print('People who were present are : '+str(b))
