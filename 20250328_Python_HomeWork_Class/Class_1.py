# ЗАДАЧА:
# Написать свой класс для хранения информации о человеке: фамилия, имя, отчество, дата рождения
# Написать свой класс для хранения информации об автомобиле: фирма, модель, год выпуска, объем двигателя, цвет
# Написать свой класс для хранения информации о единице одежды: тип, фирма, цвет
# Класс Книга: Название, автор, год издания, содержание книги (пример! не надо всю копировать! Можно "Репку" в качестве примера...) 
# * Сложное: показать работу со своими классами

# В Python, Javascript

# Лучше по одному в каждом языке, чем 4 в одном и ноль в другом.
# Если не успели всё - всё равно высылайте часть!

from datetime import datetime  # для работы с датой рождения

class Chelovek:
    def __init__(self, surname, name, otchestvo, birth_year, birth_month, birth_day):
        # surname - фамилия
        # name - имя
        # otchestvo - отчество
        # birth_year, birth_month, birth_day - год, месяц и день рождения
        self.surname = surname        # сохраняем фамилию
        self.name = name              # сохраняем имя
        self.otchestvo = otchestvo  # сохраняем отчество
        # создаём дату рождения
        self.birth_date = datetime(birth_year, birth_month, birth_day)

# Проверяем как работает
num1 = Chelovek("Иванов", "Иван", "Иванович", 1955, 5, 25)
print("Фамилия: ", num1.surname)
print("Имя: ", num1.name)
print("Отчество: ", num1.otchestvo)
print("Дата рождения: ", num1.birth_date)