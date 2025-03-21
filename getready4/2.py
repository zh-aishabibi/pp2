def generate (n):
    for i in range (n,0,-1):
        yield i

a = int(input("n: "))

print(','.join(map(str, list(generate(a)))))

print (*generate(a))