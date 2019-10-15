a=input("enter a string:")
sample=[]
b=0
x=list(set(a))
x.sort()
for j in range(len(x)):
    for i in a:
        if x[j]==i:
            b+=1
    sample.append(b)
    b=0
for i in range(len(sample)):
    print(str(x[i])+'->'+str(sample[i]))
