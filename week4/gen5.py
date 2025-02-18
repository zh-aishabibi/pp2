def generate (n):
    for i in range (n , -1, -1):
        yield i 
g = int(input("enter: "))
for i in generate(g):
    print(i, end=" ")