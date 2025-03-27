class Car:
    def __init__(self, brand, year, color, power):
        # Инициализатор с параметрами
        # bфrand - марка машины 
        # year - год выпуска
        # color - цвет
        # power- мощность
        self.brand = brand
        self.year = year
        self.color = color
        self.power = power

    def __str__(self):
        # ммаагический метод для красивой печати
        # вызывася автоматически при print
        return 'Марка: ' + self.brand + ' ' + 'Год выпуска: ' + str(self.year) + ' ' + 'Цвет: ' + self.color

# Проверка 
car = Car('Лада', 1985, 'малиновый', 200)  # создаём машину
print(car)  # через __str__