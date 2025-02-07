def solve(numheads, numlegs):
    y= (numlegs - 2*numheads)//2
    x = numheads - y

    return x,y

numheads = int(input())
numlegs = int(input())

print(solve(numheads , numlegs ))