x = str(input("Enter the String:"))
a = {}

for i in x:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print("Occurences")
for j, y in a.items():
    print(j, y)
