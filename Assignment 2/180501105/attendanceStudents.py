#attendance=['Ram-P','Malar-A','Ahuja-P','Vijay-P','Harini-A']
#print("Students present")
#for a in attendance:
#   if a[-1]=='P':
#       print(a)
a=int(input('Enter the No of Students : '))
h=[]
print('Enter your string : ')
for i in range(a):
	b=input().split('-')
	if b[1] == 'P':
		h.append(b[0])
print('Students Present: ')
#print(h[0])
for j in range(len(h)):
   print(h[j])



