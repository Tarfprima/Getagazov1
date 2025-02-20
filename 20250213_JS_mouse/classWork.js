// Ждем, пока страница полностью загрузится
window.addEventListener('load', main_function);

function main_function() {
    console.log('Страница готова');

    // Вешаем обработчик события на кнопку
    sumButton.addEventListener('click', function () {
        
        // Вычисляем сумму
        const sum = input1.value + input2.value;

        // Выводим сумму в консоль
        console.log('Сумма:', sum);
    });
}