def generate(n):
    for i in range(1,n+1):
        yield i**2

n = int(input("Enter a number: "))
for x in generate(n):
    print(x, end=" ")