pa=[]
n=int(input("enter the no of strings:\n")) 
print("enter the string:")
for i in range(n):
    x= input().split("-")
    pa.append(x[0])
    pa.append(x[1])
print(pa)
y=len(pa)
print("present students list:\n")
for i in range(0,y,2):
    if pa[i+1]=="p":
         print(pa[i]," ")
     
       


