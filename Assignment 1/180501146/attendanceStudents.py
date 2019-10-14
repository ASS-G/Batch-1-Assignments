list1=[]
list2=[]
list3=[]
n=int(input("enter the total no. of student:"))
print("\n enter name:")
for i in range(0,n):
    a=str(input())
    list1.append(a)
print("\n enter if student is present or not:")
for i in range(0,n):
    name=str(input())
    list2.append(name)
for i in range(0,n):
    if list2[i]=="P":
        list3.append(list1[i])
print("\n the present students were: \n" + str(list3))

