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