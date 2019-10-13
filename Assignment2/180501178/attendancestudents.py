total_stud=int(input("Enter the total no of students: "))
a=[]
print("Enter your string: ")
for i in range (total_stud):
    m=input().split('-')
    if m[1]=='p':
        a.append(m[0])
        print("The present students were: ")
        for name in a:
            print(name, end=" ")

~
