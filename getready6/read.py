f = open("v.txt", "rt", encoding="utf-8")

print(f.readline())

print(f.read(5))

print(f.read(3))
print(f.tell()) #how many characters ffrom the beginning (position of cursor)

print(f.read())
print(f.tell())

f.seek(0)
print(f.read())

f.close()
