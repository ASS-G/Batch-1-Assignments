n = int(input("Enter the number of students:"))
print("Enter the name and P-present A-absent:")
res = []
for _ in range(n):
    stg = input()
    if(stg[-1] == 'P'):
        res.append(stg[0:-2])
print("Present students were:")
for e in res:
    print(e)
