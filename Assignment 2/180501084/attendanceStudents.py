a=[]
a=input("Enter the strings:\n")
csv=a.split(",")
n=len(csv)
pa=[]
for i in range(n):
	pa+=csv[i].split("-")
n=len(pa)
print("present students list : \n")
for i in range(0,n,2):
	if pa[i+1]=="p":
		print(pa[i],"  ")