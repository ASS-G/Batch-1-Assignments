# ref = []
# x = 26
# for i in range(0, 10):
  # ref.insert(i, x)
  # x += 1
# for i in ref:
  # print(i, end = " ")
  
count = {}
str1 = "AAb5&bCcd#$  ^d2EE"
for j in str1:
  if j in count:
    count[j] +=1
  else:
    count[j]=1
  
print (count)
