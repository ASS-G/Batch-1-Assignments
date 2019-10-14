n = int(input("No. of students: "))
attendance = {}
for i in range(0, n):
  namex = input("Student " + str(i + 1) + ": ")
  sub = namex.split('-')
  sub1 = sub[0].strip()
  sub2 = sub[1].strip()
  attendance[sub1] = sub2
print("\nThe present students were:")
for sub1 in attendance:
  if attendance[sub1] == 'P' or attendance[sub1] == 'p':
    print(sub1, end = " ")