import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt","w") as file:
        file.write(f"Это файл {letter}.txt")
print("Файлы A-Z созданы.")