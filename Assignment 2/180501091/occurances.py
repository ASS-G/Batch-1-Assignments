string=input("enter the string:")
i=0
s=[]
while(i<len(string)):
   if string[i] not in s:
      count=string.count(string[i])
      print(string[i]+"->",count)
      s.append(string[i])
      i+=1 
   else:
      i+=1
      continue

