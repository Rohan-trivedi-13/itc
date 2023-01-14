#q2
year=int(input("enter year: "))
if year<0:
    print("invalid")
elif year%100==0 and year%400==0:
    print("leap year")
elif year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")
