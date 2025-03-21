import json

#json.load() – Read JSON from a file.
# json.loads() – Convert a JSON string into a Python dictionary.
# json.dump() – Write a Python dictionary to a JSON file.
# json.dumps() – Convert a Python dictionary into a JSON string.

# i = input("name .json: ")
# try:
#     with open (i, "r", encoding="utf-8") as file:
#         cont = json.load(file) #load from json file to dict 
#         print(cont)
# except FileNotFoundError:
#     print("No such file or directory")
# except json.decoder.JSONDecodeError:
#     print("not json file")

json_string = '{"title": "Python Developer", "salary": 75000}'
a = json.loads(json_string)
print(a["title"])

data = {"brand": "Tesla", "model": "Model S", "year": 2024}
with open ("name.json", "w" ) as file:
    json.dump(data, file, indent=4)
print("done")

user_data = {"username": "john_doe", "email": "john@example.com", "active": True}
b = json.dumps(user_data, indent=4)
print(b)

employees = [
    {"name": "Alice", "role": "Engineer"},
    {"name": "Bob", "role": "Designer"},
    {"name": "Charlie", "role": "Manager"}
] #dict 
#You use json.dumps() to convert dict → JSON and json.loads() to convert JSON → dict.