import re
pattern = ".*(?P<lowunderscore>[a-z]+_[a-z]+).*"
a = input("enter a string: ")
x = re.search(pattern, a)

if x:
    print("match found", x.group("lowunderscore"))
else:
    print("no")
