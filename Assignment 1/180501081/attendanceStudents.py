n=int(input("enter the no.of students"))
attendance=[]
print("Enter your string:")
for i in range(n): 
    b=input().split('-')
    if b[1]=='P':
       attendance.append(b[0])
print("People who were present are"+str(attendance))
