import math  # для вычисления корня

class Triangle:
    def __init__(self, a, b, c):
        # проверяем, что стороны целые числа
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
            print("Стороны должны быть целыми")
            return
        # проверяем, что стороны положительные
        if a <= 0 or b <= 0 or c <= 0:
            print("Стороны должны быть положительными!")
            return
        # Проверяем, что треугольник существует
        if (a + b <= c) or (b + c <= a) or (a + c <= b):
            print("Треугольник с такими сторонами не существует")
            return
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, int):
            print("Сторона должна быть целым")
            return
        if new_a <= 0:
            print("Сторона должна быть положительной")
            return
        if (new_a + self.__b <= self.__c) or (self.__b + self.__c <= new_a) or (new_a + self.__c <= self.__b):
            print("Треугольник с такими сторонами не существует")
            return
        self.__a = new_a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, int):
            print("Сторона должна быть целым")
            return
        if new_b <= 0:
            print("Сторона должна быть положительной")
            return
        if (self.__a + new_b <= self.__c) or (new_b + self.__c <= self.__a) or (self.__a + self.__c <= new_b):
            print("Треугольник с такими сторонами не существует")
            return
        self.__b = new_b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, new_c):
        if not isinstance(new_c, int):
            print("Сторона должна быть целым")
            return
        if new_c <= 0:
            print("Сторона должна быть положительной")
            return
        if (self.__a + self.__b <= new_c) or (self.__b + new_c <= self.__a) or (self.__a + new_c <= self.__b):
            print("Треугольник с такими сторонами не существует")
            return
        self.__c = new_c

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    @property
    def area(self):
        p = self.perimeter / 2  # полупериметр
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def __str__(self):
        return "Треугольник: a=" + str(self.__a) + ", b=" + str(self.__b) + ", c=" + str(self.__c)

# Проверяем
triangle = Triangle(3, 4, 5)
print(triangle)
print("Периметр: " + str(triangle.perimeter))
print("Площадь: " + str(triangle.area))
triangle.a = 1  
triangle.b = -2  
triangle.c = "строка"  
triangle.c = 3.5  