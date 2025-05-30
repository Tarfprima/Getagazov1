# Задача: 
# Напишите свой метод, который:
# 1. Делает задачу завершённой
# 2. Проверяет, завершена ли задача?
# 3. Устанавливает новое описание.
# 4. Устанавливает новый дедлайн
# 5. Проверяет, сколько осталось дней до срока выполнения? Часов?
# 6. Сколько дней было дано на задачу?

from datetime import datetime, timedelta  # дата и время

class Task:  
    # Класс для хранения инфы о задаче
    def __init__(self, description, deadline=datetime.now() + timedelta(1)):
        self.dt             = datetime.now()  # когда задача поставлена
        self.deadline       = deadline        # срок выполнения
        self.description    = description     # описание задачи
        self.done           = False           # завершена или нет

    # 1. Метод, чтобы сделать задачу завершённой
    def complete(self): # complete - завершено 
        self.done = True  # прост меняем на True
        print("Задача завершена!")
        
    # 2. Метод, чтобы проверить, завершена ли задача
    def complete_full(self):
        if self.done == True:
            print("Да, задача уже сделана")
        else:
            print("Нет, задача ещё не завершена")
        return self.done  # возвращаем значение
    
    # 3. Метод, чтобы установить новое описание
    def set_description(self, new_description):
        self.description = new_description  # обновляем описание
        print("Новое описание задачи: ", self.description)

    # 4. Метод, чтобы установить новый дедлайн
    def set_deadline(self, new_deadline):
        self.deadline = new_deadline  # новый срок
        print("Новый дедлайн: ", self.deadline)



# Проверяем, как работает
task = Task("Написать программу")  # создаём задачу
print("Описание: ", task.description)
print("Дедлайн: ", task.deadline)
        
task.complete()          # завершаем задачу
task.complete_full()           # проверяем, завершена ли

task.set_description("Написать игру")  # меняем описание
task.set_deadline(datetime(2025, 4, 1))  # новый дедлайн