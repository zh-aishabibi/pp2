thisset = {"apple", "banana", "cherry", "kiwi"}
thisset.remove("banana") #If the item to remove does not exist, remove() will raise an error
print(thisset)


thisset.discard("apple") #If the item to remove does not exist, discard() will NOT raise an error
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #pop() method to remove a random item
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


del thisset #delete the set completely