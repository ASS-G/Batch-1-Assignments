
def freq(arr):
    count = 0;
    arr.sort()
    for i in range(len(arr)):
        if(arr[i] == arr[(i+1)%len(arr)]):
            count += 1;
        else:
            print(arr[i]+"->"+str(count+1))
            count = 0


stg = input("Enter the string:")
arr = [e for e in stg]
print("Occurances:")
freq(arr)


