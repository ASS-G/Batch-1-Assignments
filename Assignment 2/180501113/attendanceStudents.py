csv = input("Enter name - attendance status (enter multiple values using comma): ")
s = csv.split(',')
for i in range(len(s)):
    if s[i].find("P"):
        print(s[i].split('-'))
    else:
        pass