lst=[]
n=int(input("Enter the number of students :"))
for i in range(n):
	name=input("Enter name")
	lst.append(name)
print(lst)
for i in lst:
	if  i.endswith('P'):
		print(i.split("-")[0])
	if  i.endswith('p'):
		print(i.split("-")[0])
		
	
	
	
