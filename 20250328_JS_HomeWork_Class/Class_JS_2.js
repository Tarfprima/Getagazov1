// ЗАДАЧА: 
// Написать свой класс для хранения информации о человеке: фамилия, имя, отчество, дата рождения
// Написать свой класс для хранения информации об автомобиле: фирма, модель, год выпуска, объем двигателя, цвет
// Написать свой класс для хранения информации о единице одежды: тип, фирма, цвет
// Класс Книга: Название, автор, год издания, содержание книги (пример! не надо всю копировать! Можно "Репку" в качестве примера...) 
// * Сложное: показать работу со своими классами

// В Python, Javascript

// Лучше по одному в каждом языке, чем 4 в одном и ноль в другом.
// Если не успели всё - всё равно высылайте часть!

// Запускаем код при загрузке страницы
window.addEventListener('load', function() {
    // Создаем объект для хранения информации об автомобиле
    let car = {
        firm: 'Audi',       // Фирма
        model: 'Q7',        // Модель
        year: 2020,         // Год выпуска
        engine: 3.5,        // Объем двигателя
        color: 'Белый'      // Цвет
    };
    
    // Выводим информацию об автомобиле
    console.log('Фирма: ' + car.firm);
    console.log('Модель: ' + car.model);
    console.log('Год выпуска: ' + car.year);
    console.log('Объем двигателя: ' + car.engine);
    console.log('Цвет: ' + car.color);

});