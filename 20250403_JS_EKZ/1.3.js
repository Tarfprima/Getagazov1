// Запускаем код при загрузке страницы
window.addEventListener('load', function() {
    // Дано число 7
    let number = 7;
    // счетчик вычитаний
    let count = 0;
    // пока число больше 0, вычитаем случайное значение
    while (number > 0) {
        let matemat = Math.round(Math.random()); // 0 или 1
        number = number - matemat;
        count = count + 1; // Увеличиваем счетчик
    }
    // Выводим количество вычитаний
    console.log('Сколько сделано вычитаний: ' + count);
});