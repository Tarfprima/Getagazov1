// Задача:
// Напишите свой метод, который (один пункт - один метод!)…

// 1. Делает задачу завершённой
// 2. Проверяет, завершена ли задача?
// 3. Устанавливает новое описание.
// 4. Устанавливает новый дедлайн
// 5. Проверяет, сколько осталось дней до срока выполнения? Часов?
// 6. Сколько дней было дано на задачу?
// 7. ** Супер-пупер сложно: попадали ли в дни выполнения сб, вс, праздники? Сколько дней было на задачу с учётом праздников и выходных?
// Покажите работу методов.

// Запускаем код при загрузке страницы
window.addEventListener('load', function() {
    // объект
    let task = {
        dt: new Date(), // Когда задача поставлена
        deadline: new Date(), // cрок задачи
        description: 'Написать программу',
        done: false
    };
    
    // Устанавливаем начальный срок (сегодня + 1 день)
    let num1 = task.deadline.getDate();
    task.deadline.setDate(num1 + 1);
    
    // Печатаем начальные данные
    console.log('Описание: ' + task.description);
    console.log('Дедлайн: ' + task.deadline);
    
    // 1. Функция завершения задачи
    function complete() {
        task.done = true;
        console.log('Задача завершена!');
    }
    
    // 2. Функция проверки завершения
    function konec() {
        if (task.done == true) {
            console.log('Да, задача сделана');
        } else {
            console.log('Нет, задача не завершена');
        }
        return task.done;
    }
    
    // 3. Функция установки нового описания
    function setDes(newDescription) { 
        task.description = newDescription;
        console.log('Новое описание задачи: ' + task.description);
    }
    
    // 4. Функция установки нового дедлайна
    function setDeadline(newDeadline) {
        task.deadline = newDeadline;
        console.log('Новый дедлайн: ' + task.deadline);
    }
    
    // Проверяем работу функций
    complete(); // Завершаем задачу
    konec(); // Проверяем завершение
    
    setDes('Написать игру'); // Меняем описание
    setDeadline(new Date(2025, 4, 5)); // Новый дедлайн (1 апреля 2025)
    
});
// Смог решить до 4 пункта 
// 3-4 пункт решал дольше всего, поздно дошло что можно использовать "setDes(newDescription)"