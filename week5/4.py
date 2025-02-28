import re
pattern = ".*[A-Z]{1}[a-z]+.*"
txt = input("Enter a string: ")
matches = re.search(pattern, txt)

if matches:
    print(f"Yes, matches found:{matches}, {matches}")
else:
    print("No match")
