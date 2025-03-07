import os
path=input("Введите путь к файлу: ")
if os.path.exists(path):
    if os.access(path,os.W_OK):
        os.remove(path)
        print("Файл удален.")
    else:
        print("Нет прав на удаление.")
else:
    print("Файл не найден.")
    