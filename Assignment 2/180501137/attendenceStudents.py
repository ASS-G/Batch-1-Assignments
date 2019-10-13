namelist=[]
a=[]
b=[]
n=int(input("enter the number of students:"))
print("\nEnter names of the students:")
for i in range(0,n):
  nlist=str(input())
  namelist.append(nlist)
print("\nEnter if p/a")
for i in range(0,n):
  listsd=str(input())
  a.append(listsd)
for i in range(0,n):
  if a[i]=="p" or a[i]=="P":
    b.append(namelist[i])
print ("\nThe present students are:"+ str(b))
