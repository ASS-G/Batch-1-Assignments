attdlist = ['Leena-P','Steve-A','Dinesh-P','Pragya-P']
print("the present students:")
for e in attdlist:
    if e[-1]=='P':
        print(e[0:-2])