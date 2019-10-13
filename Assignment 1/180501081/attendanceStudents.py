l=[]
n=int(input("Enter no. of student:"))
print("Enter your string(name):")
for i in range(0,n):
    a=str(input())
    l.append(a)
print("people who were  present are :")
for m in l:
    k="P" in m
    if(k):
        print(m[0:-2],end="  ")
