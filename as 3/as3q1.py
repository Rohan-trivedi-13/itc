#q1
str1=input("Enter string: ")
lst1=list(str1.split(" "))
lst2=list(set(lst1))
for i in lst2:
    if len(lst1)!=1:
        print(i,"occurs",lst1.count(i),"times")
    else:
        lst3=list(lst1[0])
        lst4=list(set(lst3))
        for j in lst4:
            print(j,"occurs",lst3.count(j),"times")
    


