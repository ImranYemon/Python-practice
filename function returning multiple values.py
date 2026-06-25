# create a function that returns both the area and circumference of a circle given it's redius

import math
def circle(redius):
    redius= int(input("redius : "))
    area = 2*math.pi*redius
    circumference = math.pi*(redius**2)

    
    return area , circumference 
print (circle(2))
