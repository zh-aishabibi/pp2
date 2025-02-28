import re 
txt = input("enter a string: ")
pattern = '.*(?P<name>a+b*).*'
x = re.search(pattern, txt)

if x:
    print ("match found!", x.group("name"))
else:
    print("no match")

