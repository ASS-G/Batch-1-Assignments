namelist=[]
list2=[]
list3=[]
n=int(input("enter the number of students:"))
print("\nEnter their names:")
for i in range(0,n):
  nlist=str(input())
  namelist.append(nlist)
print("\nEnter if p/a")
for i in range(0,n):
  listpa=str(input())
  list2.append(listpa)
for i in range(0,n):
  if list2[i]=="p" or list2[i]=="P":
    list3.append(namelist[i])
print ("\nThe present students are:"+ str(list3))

