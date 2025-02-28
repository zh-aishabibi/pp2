import re
txt = input("enter: ")

result = ""
for i in range (len(txt)):
    if txt[i] == '_':
        result += txt[i+1].upper()
        i +=1
    else:
        result += txt[i]

x = re.sub(r"_", "", result)
print(x)

'''
import re
txt = input("Enter a string in snake_case: ")
camel_case = re.sub(r'_(\w)', lambda match: match.group(1).upper(), txt)
camel_case = camel_case[0].lower() + camel_case[1:]
print(f"CamelCase: {camel_case}")
'''

