string1 = input('Enter the String: ')
lst = []
i=0
for i in range(len(string1)):
    if string1[i] in lst:
        pass
    else:
        print(string1[i] + '->' + str(string1.count(string1[i])))
        lst.append(string1[i])







