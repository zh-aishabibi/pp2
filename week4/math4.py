import math 
def paral(a,b):
    c = float(a*b)
    return math.fabs(c) 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(paral(a,b))

