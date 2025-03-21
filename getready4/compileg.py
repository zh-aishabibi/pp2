#compile(source, filename, mode)
def generate (n):
    while True:
        n +=1
        yield n

gen = generate(5)
for _ in range(10):
    print (next(gen))