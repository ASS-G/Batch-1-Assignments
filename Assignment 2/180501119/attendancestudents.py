list=[]
n = int(input("Enter number of inputs : "))
print('Enter the String:')
for i in range(0,n):
 stud = input().split('-')
 if stud[1]=='P':
     list.append(stud[0])
print('the students who were present are:')
for i in range(len(list)):
       print(list[i],end=" ")
