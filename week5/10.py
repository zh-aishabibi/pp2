import re
txt = input("enter a string: ")
x = re.sub(r'([A-Z])', r'_\1', txt )
x = re.sub(r'_(\w)', lambda match: '_' + match.group(1).lower(), x)
print(x)