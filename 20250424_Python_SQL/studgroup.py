# -------ЗАДАНИЕ----------------------------------------------
# Сделать code-review!

# Проблемы в коде, которые надо исправить:

# строка 69 - массив создан вручную. Если
# это будет условно Большой Театр, замучаетесь создавать None
# Надо сделать циклами!

# Строка 67: максимальная длина имени "вбита вручную" - 
# надо её найти 
# --------CodeReviev-------------------------------------------
# 1. Для решения задачи с массивами (строка  69) должно помочь следующие: зададим кол-во рядов и мест переменными (num_1 и num_2), а затем создадим массив с помощью циклов.
# вообщем заменим фиксированный массив на динамический. Например, так:
# num_1 = 4  # Количество рядов
# num_2 = 4  # Количество мест в ряду
# students = [[None for _ in range(num_2)] for _ in range(num_1)]

# как это доллжно работать:
# "for _ in range(num_1)]" создаёт num_1 рядов.
# "[None for _ in range(num_2)]"" заполняет каждый ряд num_2 элементами None.
# Если нужно больше мест или рядов, просто меняешь значения num_1 и num_2.

# 2. Автоматическое вычисление max_name (строка 67)
# для решение надо бы пройти по всем именам в данных и найти самое длинное. это должно помочь
# после получения данных из базы "(data = cursor.fetchall())", вычислим max_name. пример:
# max_name = max(len(s[0]) for s in data) 
# s[0] — имя студента из кортежа data 
# len(s[0]) — длина имени.
# max находит максимальную длину среди всех имён. 
# max — искал в гугле и нашел это, "max" это вроде стандартная функция python которая например может найти самую длинную строку.
# не сказал бы что очень хорошо его изучил, но понимания как оно примерно работает есть. 
# на этом сайте прочел: https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-max/


def get_raw_data():
    import psycopg

    # Подключиться к БД

    conn = psycopg.connect(
        dbname='students',
        user='wera',
    )
    print(conn)
    cursor = conn.cursor()

    # Прочитать

    cursor.execute('SELECT first_name, row_number, comp FROM group411 WHERE NOT comp IS NULL')  # ; не обязательна в отличие от консоли!
    # Достать сразу все данные из запроса
    data = cursor.fetchall()

    # Отключиться
    cursor.close()
    conn.close()
    return data

# [('Софья', 2, 4), 
# ('Ульяна', 3, 4), 
# ('Рустам', 2, 1), 
# ('Артур', 1, 3), 
# ('Константин', 3, 2), 
# ('Андрей', 1, 2)]

def understand(data):
    max_name = 10
    print(data)
    students = [[None, None, None, None],  # 0 - 4 парта
                [None, None, None, None],  # 1 - 3 парта
                [None, None, None, None],  # 2 - 2 парта
                [None, None, None, None]]  # 3 - 1 парта (перед учителем)
    for s in data:
        name, row, comp = s
        students[row - 1][comp - 1] = name

    return students, max_name

def draw(classroom, max_name):
    line = '+' + 4 * ('-' * max_name + '+')
    print(line)
    for row in classroom:
        row_str = '|'
        for chair in row:
            if chair:
                row_str += ('%%%is' % max_name) % chair + '|'
            else:
                row_str += ' ' * max_name + '|'
        print(row_str)
        print(line)

def update(name, row, comp):
    import psycopg

    # Подключиться к БД

    conn = psycopg.connect(
        dbname='students',
        user='wera',
    )
    cursor = conn.cursor()

    # Записать и подтвердить

    cursor.execute("UPDATE group411 SET row_number=%i, comp=%i WHERE first_name='%s'" % (
        row, comp, name  # Если имена повторяются, будет неправильная БД!
    ))  # ; не обязательна в отличие от консоли!
    conn.commit()  # Подтвердить изменения

    # Отключиться
    cursor.close()
    conn.close()

update('Андрей', 1, 2)
draw(
    *understand(
        get_raw_data()))