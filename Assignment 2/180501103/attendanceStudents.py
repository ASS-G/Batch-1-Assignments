list=[]
n=int(input("Enter number of inputs:"))
print('Enter the string:')
for i in range(0,n):
    s=input().split('-')
    if s[1]=='P':
        list.append(s[0])
    print('Students who were present are:')
    for i in range(len(list)):
        print(list[i],end=" ")

