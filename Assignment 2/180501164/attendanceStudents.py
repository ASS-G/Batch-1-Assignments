n = int(input("Enter the number of students:"))
print("Enter the name and P-present A-absent:")
a_string="The students present were:\n"
for x in range (0,n):
    s=raw_input();
    length=len(s)
    if s[length-1]=='P':
        a_string=a_string+s[0:-2]+" "
print (a_string)

