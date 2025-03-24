# ЗАДАНИЕ: 1. В файле сохранены фамилии тех, кто был на субботнике,
# через запятую. Например: Иванов, Петров, Сидоров
# Пользователь вводит свою фамилию. Компьютер должен ответить
# "был" или "нет"

# 2. Записать новый файл, в котором фамилии будут каждая на новой строке

# 3. Решить предыдущую задачу, прочитав все фамилии в список,
# а затем записать в файл без использования цикла

# ------------------------------ 1 ----------------------------

# Проверяем, был ли человек на субботнике
# Файл с фамилиями через запятую

f = open('subbotnik.txt')  # Открываем файл
vse = f.read()  # читаем всё из файла в строку
f.close()  # закрываем файл

# Спрашиваем фамилию у пользователя
fam = input('Введи свою фамилию: ')

# Проверяем, есть ли фамилия в строке
if fam in vse:
    print('Был')
else:
    print('Нет')
    
# ------------------------------ 2 ----------------------------

# Переписываем фамилии в новый файл, каждая на новой строке

f = open('subbotnik.txt')  # открываем старый файл
vse = f.read()  # читаем всё
f.close()

# Разделяем строку по запятым
fam_list = vse.split(',')  # получаем список фамилий

# Открываем новый файл для записи
f2 = open('subbotnik_new.txt', 'w')
# Проходим по списку и пишем каждую фамилию
for fam in fam_list:
    f2.write(fam)  # пишем фамилию
    f2.write('\n')  # добавляем новую строку
f2.close()

# ------------------------------ 3 ----------------------------

# Читаем фамилии в список и записываем без цикла

f = open('subbotnik.txt')  # Открываем старый файл
vse = f.read()  # читаем всё
f.close()

# Разделяем по запятым и убираем лишнее
fam_list = vse.split(',')  # делаем список 

# Спрашиваем фамилию
fam = input('Введи свою фамилию: ')
if fam in fam_list:  # проверяем, есть ли в списке
    print('Был')
else:
    print('Нет')

# пишем список в файл без цикла
f2 = open('subbotnik_new.txt', 'w')
text = '\n'.join(fam_list)  # склеиваем список с новой строкой 
f2.write(text)  # пишем сразу всё
f2.close()