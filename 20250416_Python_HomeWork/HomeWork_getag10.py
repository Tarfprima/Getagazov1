# Создайте класс Печатное Издание
# У него есть название и год издания

# Унаследуйте печатное издание, создав классы
# Книга, Журнал

# У книги есть автор,
# у журнала есть издательство, номер и периодичность выхода

# Создайте массив за 5 лет ежемесячных журналов "Работница" c 2015 года
# Создайте массив из 3 разных книг

# Запишите массивы в файл, создайте функции записи в файл
# 1. Печатного издания, книги, журнала, используя super()

# Класс Печатное Издание
class book2:
    def __init__(self, name, year):
        self.__name = name  # название
        self.__year = year  # год издания

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return "Название: " + self.__name + ", Год: " + str(self.__year)

# класс книга, наследуется от печатного издания
class Book(book2):
    def __init__(self, name, year, avtor):
        super().__init__(name, year)
        self.__avtor = avtor  # автор

    @property
    def avtor(self):
        return self.__avtor

    def __str__(self):
        return super().__str__() + ", Автор: " + self.__avtor

# класс журнал, наследуется от печатного издания
class Magazine(book2):
    def __init__(self, name, year, num4, num5, num6):
        super().__init__(name, year)
        self.__num4 = num4  # издательство
        self.__num5 = num5  # номер
        self.__num6 = num6  # периодичность

    @property
    def num4(self):
        return self.__num4

    @property
    def num5(self):
        return self.__num5

    @property
    def num6(self):
        return self.__num6

    def __str__(self):
        return super().__str__() + ", Издательство: " + self.__num4 + ", Номер: " + str(self.__num5) + ", Периодичность: " + self.__num6

# Функции записи в файл
def record(num7, num8):
    try:
        num9 = open(num8, "a")
        num9.write(str(num7) + "\n")
        num9.close()
    except FileNotFoundError:
        print("Не удалось открыть файл " + num8)

def book3(num10, num11):
    try:
        num12 = open(num11, "a")
        num12.write("Книга: " + str(num10) + "\n")
        num12.close()
    except FileNotFoundError:
        print("Не удалось открыть файл " + num11)

def book4(num13, num14):
    try:
        num15 = open(num14, "a")
        num15.write("Журнал: " + super(Magazine, num13).__str__() + "\n")
        num15.close()
    except FileNotFoundError:
        print("Не удалось открыть файл " + num14)

# массив журналов "Работница" за 5 лет (2015-2019), ежемесячные
num16 = []
num17 = 1  # Номер журнала
for num18 in range(2000, 2006):  
    for num19 in range(1, 13):  
        num20 = Magazine("Работница", num18, "Издательство Работница", num17, "ежемесячный")
        num16.append(num20)
        num17 = num17 + 1

# массив из 3 книг
num21 = [
    Book("Война и мир", 1865, "Лев Толстой"),
    Book("Преступление и наказание", 1866, "Фёдор Достоевский"),
    Book("Гарри Поттер", 1997, "Дж. К. Роулинг")
]

# Записываем журналы в файл
for num22 in num16:
    book4(num22, "magazines.txt")

# Записываем книги в файл
for num23 in num21:
    book3(num23, "books.txt")