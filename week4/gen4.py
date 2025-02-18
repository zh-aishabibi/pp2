def generate (a,b):
    for i in range (a,b+1,1):
        yield i**2

start = int(input("where to start?: "))
end = int(input("where to end?: "))

for i in generate(start, end):
    print (i, end=" ")

