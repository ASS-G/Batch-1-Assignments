final=[]
for i in range(0,5):
  names=str(input("Enter your string"))
  a=names.split("-")
  if(a[1]=='p' or a[1]=='P'):
   final.append(a[0])
print("The present students were :")
for x in range(len(final)):
   print(final[x])