string=input('enter the string: ')
i=0
temp={}
print("occurances: ")
while(i<len(string)):
    if string[i] not in temp:
        count=string.count(string[i])
        print(string[i]+"->",count)
        temp.append(string[i])
        i+=1
    else:
        i+=1
        continue
