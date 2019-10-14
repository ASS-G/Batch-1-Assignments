st=input("Enter the string")
temp={}
a=list(st)
for i in st: 
    if i in temp: 
      temp[i] += 1
    else: 
        temp[i] = 1
    #for x in range(len(a)): 
for key,value in temp.items():
    print (str(key) + " -> " + str(value))
    #print ("Occurances:\n "+str(temp[x]))
