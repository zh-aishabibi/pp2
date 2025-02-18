def generate (n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n= int(input("enter a number: "))
for even in generate(n):
    if (even==n-1):
        print(n-1)
    elif (even == n):
        print(n)
    else:
        print (even, end=",")