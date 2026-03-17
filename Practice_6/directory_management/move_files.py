import os
#os.getcwd()  # Получение текущей рабочей директории
path = os.getcwd()
print(path)  # Вывод: C:\Users\User\Project или /home/user/project
#os.chdir(path) # Изменение текущей рабочей директории
os.chdir('/tmp') # Изменение текущей рабочей директории на /tmp
print(os.getcwd())  # Вывод: /tmp
#os.mkdir('new_folder')  # Создание новой папки
os.mkdir('new_folder')
#os.makedirs('new_folder/sub_folder')  # Создание вложенных папок
os.makedirs('new_folder/sub_folder')
#os.listdir(path)  # Получение списка файлов и папок в текущей директории
print(os.listdir(path))  # Вывод: ['file1.txt', 'file2.txt', 'new_folder']