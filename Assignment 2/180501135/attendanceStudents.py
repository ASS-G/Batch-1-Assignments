print("Enter Names of 5 students:(ex: Harini-P):")
for j in range(5):
    name = raw_input()
    s.append(name)
print('The present students were:')
b=0
print("The present students were:")
for i in s:
    k=s[b]
    if k[-1]=='P':
        print(k[:-2]);
    b+=1;
        

        

