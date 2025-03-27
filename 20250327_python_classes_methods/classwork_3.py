class Car:
    def __init__(self, brand, year, color, power):
        # Инициализатор с параметрами
        # bфrand - марка машины 
        # year - год выпуска
        # color - цвет
        # power --- мощность
        self.brand = brand
        self.year = year
        self.color = color
        self.power = power

    def __str__(self):
        # ммаагический метод для красивой печати
        # вызывася автоматически при print
        # длаем строку с переносами строк (\n)
        return 'Марка: ' + self.brand + '\n' + 'Год выпуска: ' + str(self.year) + '\n' + 'Цвет: ' + self.color

# Проверка 
car = Car('Лада', 1999, 'малиновый', 99)  # создаём машину
print(car)  # через __str__