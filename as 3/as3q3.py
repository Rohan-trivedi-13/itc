lst=[]
num=int(input("enter number of elements in list: "))
for i in range(num):
    a=int(input("enter a number: "))
    lst.append(a)

lst2=[]
for j in lst:
    lst2.append((j,j*j))

print(lst2)
