n=int(input('Enter the No of Students : '))
list=[]
print('Enter your string : ')
for i in range(n):
    name=input().split('-')
    if name[1] == 'P':
        list.append(name[0])
print('People who were present are : ')
for name in list:
    print(name, end =" ")
