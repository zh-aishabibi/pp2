import os

copy = input("what to copy ")
name = input("name: ")

file = f'{name}.txt'

if os.path.exists(copy):
    with open(copy, "rt") as d:
        content = d.read()
    with open (file, 'w') as f:
        f.write(content)