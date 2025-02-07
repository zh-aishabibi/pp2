import itertools 

def per():
    str = input()
    p = [''.join(n) for n in (itertools.permutations(str))] #tuple
    return p

print(per())