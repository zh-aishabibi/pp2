import re

txt = input("cd: ")

x = re.sub(r'([A-Z])' , lambda m: '_' + m.group(1).lower() , txt) 

print(x)