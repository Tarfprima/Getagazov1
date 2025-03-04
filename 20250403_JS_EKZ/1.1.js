// Запускаем код при загрузке страницы
window.addEventListener('load', function() {
    // У меня на карте 50 тысяч рублей
    let money = 50000;
    // Спрашиваем стоимость телефона через prompt
    let price = prompt('Сколько стоит телефон, который вы хотите купить?');
    // Преобразуем строку из prompt в число
    let phonePrice = Number(price); 
    // Проверяем, хватает ли денег
    if (phonePrice <= money) {
        console.log('да, покупайте');
    } else {
        console.log('нет, не хватает денег');
    }
});