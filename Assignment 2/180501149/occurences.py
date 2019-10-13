value=input("Enter the string:")
all_freq={}
for i in value:
  if i in all_freq:
   all_freq[i]+=1
  else:
    all_freq[i]=1
print("\nThe count of occurences are:\n"+str(all_freq))


