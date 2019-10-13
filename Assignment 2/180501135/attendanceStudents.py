s = ["Ram-P", "Malar-A", "Ahuja-P", "Vijay-P", "Harini-A"]
print('The present students were:')
b=0
print("The present students were:")
for i in s:
    k=s[b]
    if k[-1]=='P':
        print(k[:-2]);
    b+=1;
        
