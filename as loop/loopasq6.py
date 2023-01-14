#q6
a=int(input("enter lower limit"))
for i in range(a,int(input("Enter upper limit: "))):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)


            
        
