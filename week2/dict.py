thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "colors": ["red", "white", "blue"],
  "year": 1964  #cannot have two items with the same key
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)