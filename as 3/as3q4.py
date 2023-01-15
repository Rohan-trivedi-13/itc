#q4
gp=int(input("Enter grade [4-10]: "))
if gp==10:
    p="Outstanding"
    g="A+"
elif gp==9:
    p="Excellent"
    g="A"
elif gp==8:
    p="Very Good"
    g="B+"
elif gp==7:
    p="Good"
    g="B"
elif gp==6:
    p="Average"
    g="C+"
elif gp==5:
    p="Below Average"
    g="C"
elif gp==4:
    p="Poor"
    g="D"
else:
    print("Error")
print("Your grade is",g, "and",p, "Performance")