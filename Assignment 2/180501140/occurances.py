value=input("Enter the string:")
number={}
for i in value:
  if i in number:
   number[i]+=1
  else:
    number[i]=1
print("\nThe count of occurences are:\n"+str(number))

