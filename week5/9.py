import re
txt = input("enter a string: ")

x = re.sub(r'([A-Z])', r' \1', txt )
print(x)