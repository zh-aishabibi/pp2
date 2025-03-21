import re

txt = input("cd: ")

x = re.sub(r"_([a-z])" , lambda m: m.group(1).upper(), txt) 

print(x) #what is inside () it is our group 