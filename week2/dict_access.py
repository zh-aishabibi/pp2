thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model") #same result
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)


