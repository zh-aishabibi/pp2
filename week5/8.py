import re
txt = input("enter a string: ")
x = re.split(r'(?=[A-Z])', txt)
print(x)
