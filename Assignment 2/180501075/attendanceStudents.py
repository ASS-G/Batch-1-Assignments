list = []



n = int(input("Enter the no.of.inputs : "))



print('Enter your String:')



for i in range(0,n):



    stu = input().split('-')



    if stu[1]=='P':



        list.append(stu[0])



print('The present students were:')



for i in range(len(list)):



        print(list[i],end=" ")
