# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_dir (name_dir):
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(dir_path)
        print('Папка создана')
    except FileExistsError:
        print('Такая директория уже существует')

i = 1
while i <= 9:
    create_dir('dir_' + str(i))
    i += 1

def remove_dir (name_dir):
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(dir_path)
        print('Папка удалена')
    except FileNotFoundError:
        print('Такой директории не существует')

file_list = os.listdir()
for di in file_list:
    if di.startswith('dir_'):
        remove_dir(di)
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!


file_list = os.listdir()
list = [file_list[i] for i in range(len(file_list)) if os.path.isdir(file_list[i])]
print(list)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

import shutil
file = os.path.join(os.getcwd(), 'easy.py')
new_file = file + '.copy'
shutil.copy(file, new_file)