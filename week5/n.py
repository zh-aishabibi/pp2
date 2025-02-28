import re

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r"\nБИН\s(?P<BIN>[0-9]+)"
x =re.search(pattern, text)

print(x.group("BIN"))