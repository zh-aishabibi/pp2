import os
print("1) ",os.getcwd())
print("2)",os.mkdir('folder'))
if not os.path.isdir('folder'):
    print("такой фолдер уже существует!")