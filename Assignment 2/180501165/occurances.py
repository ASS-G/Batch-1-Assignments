test_str=input("enter the string:")
freq={}
for i in test_str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print("Occurances\n"+str(freq))
        

