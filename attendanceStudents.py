l=[]
x=int(input("Enter no of student"))
print("Enter your string")
for i in range(0,x):
    a=str(input())
    l.append(a)
print("The student present were:")
for j in l:
    z="P" in j
    if(z):
        print(j[0:-2],end="  ")
