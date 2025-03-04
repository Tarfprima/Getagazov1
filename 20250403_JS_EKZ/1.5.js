// Запускаем код при загрузке страницы
window.addEventListener('load', function() {
    // Цена за ночь в отеле
    let pricePerNight = 2500;
    // Выводим цену за ночь
    console.log('Цена за ночь: ' + pricePerNight);
    // Запрашиваем количество ночей
    let nights = prompt('Сколько ночей?');
    // Преобразуем строку в число и вычисляем сумму
    let total = pricePerNight * Number(nights);
    // Выводим сумму к оплате
    console.log('Сумма к оплате: ' + total);
});
// pricePerNight - ценаЗаНочь
// total - итого