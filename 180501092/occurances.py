s: str = input("Enter the String:")
l = len(s)
i=0
j=i
for i in range (len(s)):
    c = s.find(s[i])+1
    print(s[i]+"->"+str(c))
