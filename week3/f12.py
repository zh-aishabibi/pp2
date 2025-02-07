def hist(n):
    v = '*'
    return v* n

n = input()
lst = [int(x) for x in n.split()]
for i in lst:
    print (hist(i))

    


