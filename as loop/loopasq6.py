#q6
for i in range(2,int(input("Enter upper limit: "))):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

            
        
