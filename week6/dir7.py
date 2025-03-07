source=input("Введите имя исходного файла: ")
destination=input("Введите имя целевого файла: ")
try:
    with open(source,"r",encoding="utf-8") as src,open(destination,"w",encoding="utf-8") as dest:
        dest.write(src.read())
    print("Файл скопирован.")
except FileNotFoundError:
    print("Исходный файл не найден.")