n=int(input("Enter the no.of students:"))
attendance=[]
print("enter your string:")
for i in range(n):
   b=input().split('-')
   if b[1]=='P':
      attendance.append(b[0])
print("People who were present are:")
for name in attendance:
    print(name,end = " ")

