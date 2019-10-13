string = input('Enter the String: ')



list = []



i=0



print('Occurances:')



for i in range(len(string)):



    if string[i] in list:



        pass



    else:



        print(string[i] + '->' + str(string.count(string[i])))



        list.append(string[i])
