input_string = input('Enter the String: ')
characters = []
charcount = []

for i in input_string:
    if i not in characters:
        characters.append(i)
        charcount.append(1)
    else:
        k = characters.index(i)
        charcount[k] += 1

for i in range(len(characters)):
    print( characters[i] + "->" + str(charcount[i]) )
