n=int(input('Enter the number of students:'))
attendance=[]
print('Enter the string :')
for i in range(n):
    b=input().split('-')
    if b[1] == 'P':
        attendance.append(b[0])
print('Peaple who were present are: ')
for name in attendance:
    print(name, end=" ")   
