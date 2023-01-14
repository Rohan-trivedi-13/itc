#q2
stp=int(input("enter starting point"))
rng=range(stp,int(input("enter ending point")))
num=int(input("enter a number"))
for i in rng:
    if i%num==0:
        print(i)