namelist=[]
list2=[]
list3=[]
n=int(input("enter the total number of students:"))
print("\nEnter their names of the students:")
for i in range(0,n):
  nlist=str(input())
  namelist.append(nlist)
print("\nEnter if the student is present or not as p/a")
for i in range(0,n):
  listname=str(input())
  list2.append(listname)
for i in range(0,n):
  if list2[i]=="p" or list2[i]=="P":
    list3.append(namelist[i])
print ("\nThe present students were:\n"+ str(list3))

