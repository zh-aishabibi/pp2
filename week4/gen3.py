def generate (n):
    for i in range(0,n+1):
        if i%12== 0:
            yield i

n = int(input("enter a number to check its div by 3 and 1: "))
for x in generate(n):
    print (x , end=" ")