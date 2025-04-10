from datetime import datetime

# Класс Human 
class Human:
    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        print('Тут вообще-то работает функция!')
        return datetime.now().year - self.__birthday.year
    
    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self, new_birthday):
        if isinstance(new_birthday, datetime):
            if new_birthday < datetime.now():
                self.__birthday = new_birthday
            else:
                print('Дата из будущего: ', new_birthday)
        else:
            print('Не является datetime: ', new_birthday, type(new_birthday))

    def __str__(self):
        return self.__name + ", " + str(self.age)

# Класс Student, наследуемый от Human
class Student(Human):
    def __init__(self, name, birthday, group, course):
        super().__init__(name, birthday)
        self.__marks = []
        self.__group = group
        self.__course = course

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_mark):
        if isinstance(new_mark, int) and 0 < new_mark < 13:
            self.__marks.append(new_mark)
        else:
            print("Оценка должна быть числом от 1 до 12, а не " + str(new_mark))

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, new_group):
        self.__group = new_group

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, new_course):
        self.__course = new_course

    # Добавил свойство metem_ocenka, которое вычисляет средний балл как сумму оценок. (Деленние на их кол-во).
    # Если нету оценок то, возвращает 0, чтобы не было деления на ноль.
    @property
    def matem_ocenka(self): 
        if len(self.__marks) == 0:
            return 0
        return sum(self.__marks) / len(self.__marks)

    def __str__(self):
        # Используем self.name вместо self.__name
        return self.name + ", " + str(self.age) + ", " + str(self.__course) + ", группа " + str(self.__group) + ", средний балл " + str(self.matem_ocenka)

# Проверяем
# Создаём человека
human = Human("Иван", datetime(1955, 7, 4))
print(human)  

# Создаём студента
student = Student("Вася", datetime(2000, 1, 1), 'python 411', "Питон")
# Добавляем оценки
student.marks = 12
student.marks = 10
student.marks = 6
student.marks = 10
student.marks = 8
student.marks = 12
student.marks = 10
print(student)  