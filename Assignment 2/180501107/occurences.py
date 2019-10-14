value=input('Enter the string')
ans={}
for i in value:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1
print('\nThe count of occurences are:\n'+str(ans))
