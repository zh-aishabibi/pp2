import math
def poly (n,s):
    area = n* s**2 /(4* math.tan(math.pi/n))
    return round(area,3)  

n = int(input("Enter a number of sides: "))
s = int(input("Enter a length of a side: "))
print(poly(n,s))