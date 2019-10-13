n=int(input('Enter the No of Students : '))
attendance=[]
print('Enter your string : ')
for i in range(n):
    b=input().split('-')
    if b[1] == 'P':
        attendance.append(b[0])
print('People who were present are : ')
for name in attendance:
    print(name, end =" ")
