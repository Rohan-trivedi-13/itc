#q7
n=int(input('enter number of terms in fibonacci sequence: '))
num1=0
num2=1
print(num1)
print(num2)
i=0
while i<n-2:
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
    i+=1
