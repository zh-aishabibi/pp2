data=["apple","banana","cherry"]
filename="output.txt"
with open(filename,"w",encoding="utf-8") as file:
    for item in data:
        file.write(item+"\n")
print("Список записан в файл.")