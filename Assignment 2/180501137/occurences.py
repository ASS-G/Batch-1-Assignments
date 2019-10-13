st=input("Enter the string:")
all_freq={}
for i in st:
  if i in all_freq:
   all_freq[i]+=1
  else:
    all_freq[i]=1
print("\nThe  occurences given string are :\n"+str(all_freq))