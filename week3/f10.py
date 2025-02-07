def unique(hislist):

    seen = []
    for i in hislist:
        if i not in seen:
            seen.append(i)
    return seen

n = input()
lst = [int(x) for x in n.split() ]

print(unique(lst))