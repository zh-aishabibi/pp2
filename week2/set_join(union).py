set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #can use the | operator instead of the union()
print(set3)


set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4) #myset = set1 | set2 | set3 |set4
print(myset)


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y) #| operator only allows you to join sets with sets
print(z)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)