x=str(input("Enter the string"))
a={}
for i in x:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print("Occurances")
for j,y in a.items():
    print(j,y)
