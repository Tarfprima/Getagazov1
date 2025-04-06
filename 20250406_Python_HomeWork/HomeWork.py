#1. Написать класс Человек
# У него должны быть поля "дата рождения", "имя"
# Написать getter и setter (при необходимости) для
# имени
# даты рождения
# возраста
# "взрослый или нет?" (18+)

# Написать магический метод str

# Создать и напечатать двух людей

from datetime import datetime  # для работы с датой

class num1:
    def __init__(self, num2, num3):
        # инит для человека
        self.__num2 = num2
        self.__num3 = num3

    # геттер для имени
    def get_num2(self):
        return self.__num2

    # сеттер для имени
    def set_num2(self, num4):
        if isinstance(num4, str):  # тест, на строку
            self.__num2 = num4
        else:
            print("Имя должно быть строкой, а не", num4)

    # геттер для даты рождения
    def get_num3(self):
        return self.__num3

    # сеттер для даты рождения
    def set_num3(self, num5):
        if isinstance(num5, datetime):  # надо проверить, что это datetime
            self.__num3 = num5
        else:
            print("Дата рождения должна быть datetime, а не", num5)

    # геттер для возраста
    def get_num6(self):
        num7 = datetime.now()  # текущая дата
        num8 = num7 - self.__num3  # разница в днях
        num9 = num8.days // 365  # делим на 365, чтобы получить годы
        return num9

    # геттер для "18+"
    def get_num10(self):
        num11 = self.get_num6()  # берём возраст
        if num11 >= 18:
            return True
        else:
            return False

    # магический метод 
    def __str__(self):
        num12 = self.get_num6()
        num13 = "взрослый"  # предполагаем, что взрослый
        if self.get_num10() == False:  # если не взрослый
            num13 = "не взрослый"
        return "Имя: " + self.__num2 + ", Дата рождения: " + str(self.__num3) + ", Возраст: " + str(num12) + ", " + num13

# Создаём двух людей
num14 = num1("Владимир", datetime(1955, 7, 18))
num15 = num1("Валентина", datetime(2012, 4, 22))

# Печатаем
print(num14)
print(num15)

# Проверяем геттеры и сеттеры
print("Возраст Владимира:", num14.get_num6())
print("Валентина совершеннолетняя?:", num15.get_num10())
