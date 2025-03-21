def generate(n):
    for i in range(0,n):
        yield i**2

a = int(input("enter a number: "))
for x in generate(a):
    print(x)