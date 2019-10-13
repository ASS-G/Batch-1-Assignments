students = []
print('Enter the Student name and enter "done" to stop')
while 1:
    name = input().split('-')
    if name[0] == 'done':
        break
    if name[1] == 'P':
        students.append(name[0])
print('The present students were: ')
for i in students:
    print(i,end=" ")
