# Задание 1: Задаем случайные вопросы на вычитание и сохраняем в файл
import random  # Берем random 

# Открываем файл на запись
f = open('subtraction_test.txt', 'w', encoding='utf-8')

# Счетчики для правильных и всех ответов
ans = 0
all_que = 28  # Зададим 28 вопросов

# Задаем 28 рандомных вопросов
for i in range(all_que):
    # генерим два числа: первое больше второго, чтобы не было отрицательных ответов
    num1 = random.randint(5, 20)  # Первое число
    num2 = random.randint(0, num1 - 1)  # второе меньше первого
    correct = num1 - num2  # правильный ответ

    # Задаем вопрос человеку
    user = input(f"{num1} - {num2} = ")

    # Проверяем ответ
    if user == str(correct):  # сравниваем как строки
        f.write(f"{num1} - {num2} = {user} верно\n")
        ans += 1  # увеличиваем счетчик правильных
    else:
        f.write(f"{num1} - {num2} = {user} неверно, {correct}\n")

# Записываем итог в файл
f.write(f"Было задано {all_que} вопросов, {ans} из них верно\n")
f.close()  
print("Вопросы и результаты записаны в 'subtraction_test.txt'!")