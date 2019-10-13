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
        

        
        
        print "Enter 5 items on shopping list"
for i in xrange(5): # range starts from 0 and ends at 5-1 (so 0, 1, 2, 3, 4 executes your loop contents 5 times)
    shopping = raw_input()
    mylist.append(shopping) # add input to the list
