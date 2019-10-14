# Attendance
n=int(input("Enter input of number of students: "))
print("Enter name of student and P for Present, A for Absent")

str=[]
for m in range(n):
	s=input()
	if(s[-1]=='P'):
		str.append(s[:-2])	# Present students in str
# Print Present students
print("Present Students were: ")
for i in str:
	print(i)
