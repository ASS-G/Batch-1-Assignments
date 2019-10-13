n=int(input('enter the no of students : '))
attendence=[]
print('enter your string : ')
for i in range(n):
    b=input() .split('-')
    if b[1] =='P':
        attendence.append(b[0])
        print('People who were present are : '+str(attendence))
