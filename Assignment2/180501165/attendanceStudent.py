names=[]
n=int(input("enter the no.of strings:"))
print("enter the string")
for i in range(n):
      ele=input()
      names.append(ele)
print("The students who are present are:")      
for i in names:
    if i.endswith('P') or i.endswith('p'): 
         print(i.split("-")[0])
     

