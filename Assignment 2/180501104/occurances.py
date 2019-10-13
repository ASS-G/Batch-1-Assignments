str=input('enter a string:')
i=0
s=[]
while(i<len(str)):
     if str[i] in s:
        i+=1
     else:
        count=str.count(str[i])
        print(str[i]+"->",count)
        s.append(str[i])
        i+=1 
