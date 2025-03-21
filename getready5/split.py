import re

txt = input("cd: ")

x = re.split("[A-Z]", txt )

print(x)