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