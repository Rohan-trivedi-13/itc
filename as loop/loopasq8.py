#q8
lst=[]
for i in range(1,11):
    lst.append(int(input("Enter a number")))
lst2=list(set(lst))

pos=[]
neg=[]
even=[]
odd=[]
for j in lst2:
    if j>0:
        pos.append(j)
    if j<0:
        neg.append(j)
    if j%2==0:
        even.append(j)
    if j%2!=0:
        odd.append(j)
    print(j," appears ",lst.count(j),"times")
print("positive numbers: ",pos, "\nnegative numbers: ",neg, "\nodd numbers: ",odd, "\neven numbers: ",even)
