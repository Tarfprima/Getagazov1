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
        
task = Task("Написать программу")
task.complete()          # завершаем задачу