#q3
a=()
b=()
c=()
import random
for i in range(1,11):
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=a*b
    print("Question",i,":",a,"*",b,"=")
    d=int(input("enter your answer: "))
    if d==c:
        print("Right!")
    else:
        print("Wrong. The answer is",c)
    i+=1

