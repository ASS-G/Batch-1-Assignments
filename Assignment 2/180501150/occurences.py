st=raw_input("Enter the string: ")
fin=[];
for i in st:
        if(i not in fin):
                print(i+"->"),
                print(st.count(i))
                fin.append(i)
