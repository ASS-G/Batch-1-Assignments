str1 = input("Enter the string: ")
times = {}
print("Occurances:\n")
for i in str1:
    if i in times:
        times[i] +=1
    else:
        times[i] = 1
print(str(times))
        






