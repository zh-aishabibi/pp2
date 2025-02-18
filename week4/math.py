import math

def torad (a):
    b = math.radians(a)
    return round(b,6)

a = float(input("Enter a number: "))
print(f"Number in radians: {torad(a)}")