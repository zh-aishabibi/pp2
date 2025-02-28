import re
txt = input("enter: ")
x = re.sub(r"[ \.,]", ":", txt)
print(x)