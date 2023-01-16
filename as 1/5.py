import math
for i in range (0,346,15):
    a=round((math.sin(i*(math.pi/180))),4)
    b=round((math.cos(i*(math.pi/180))),4)
    print(i,"---",a,b)

    
