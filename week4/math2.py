import math

def trap(a,b,h):
    area = ((a+b)/2)*h
    return math.fabs(area)

a = int(input("Enter a first base: "))
b = int(input("Enter a second base: "))
h = int(input("Enter a height: "))

print(trap(a,b,h))