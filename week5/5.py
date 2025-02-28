import re
pattern = ".*(?P<name>[a]+.*b)"

a = input("enter a string: ")
x = re.search(pattern, a)
if x:
    print ("match found!", x.group("name"))
else:
    print("no match")