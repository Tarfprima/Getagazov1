# Импортируем random для случайных чисел
import random

# Создаем пустой словарь, ключ - дата, значение - оценка 
grades = {}
# Задаем даты с 1 по 20 января 
for day in range(1, 21): # от 1 до 20 включительно 
    # формируем дату как строку
    date = f"{day} января"
    grade = random.randint(7, 12) 
    grades[date] = grade # добавляют новую пару
    
# выводим что-бы посмотреть что получилось 
print('Все оценки: ')
for date in grades:
    print(date, grades[date])

# 1. считаем среднюю оценку за весь период
sum_grades = 0 # сумма всех оценок
count_grades = 0 # кол-во оценок
for grade in grades.values(): # значения из словоря (оценки)
    sum_grades += grade # добавляем оценку к сумме 
    count_grades += 1 #увеличиваем счетчик 
average_all = sum_grades / count_grades # делим сумму на кол-во
print('Средняя оценка за период: ', average_all)

# 2. считаем среднюю оценку с 4 по 9 янв.
sum_period = 0 # сумма оценок за период
count_period = 0 # кол-во оценок в периоде
start_day = 4 # начало периода
end_day = 9 # конец периода
for day in range(start_day, end_day + 1): # от 4 до 9 включительно
    date = f"{day} января" 
    if date in grades: #Проверяем есть ли такая дата в словаре
        sum_period += grades[date] # добавляем оценку 
        count_period += 1 
        
# вычесляем среднюю оценку за период 
if count_period > 0: # проверяем есть ли оценки в периоде
    average_period = sum_period / count_period
    print(f'средняя оценка с {start_day} по {end_day} января:', average_period)
else:
    print('В указанном периоде нет оценок!')
    
#average - средний 
#grades - оценки 