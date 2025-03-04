// Сложный код,  массивы...
// Запускаем код при загрузке страницы
window.addEventListener('load', massive);

function massive() {
    // Задаем массив чисел
    let numbers = [1, 2, 3, 4, 5];
    // Переменная для суммы
    let sum = 0;
    // Считаем сумму в цикле
    for (let i = 0; i < numbers.length; i++) { // Подобный код мы уже писали с вами, на прошлых уроках, например тут: 20250227_JS_mathtest. Но там он был сложнее
        sum = sum + numbers[i];
    }
    // Выводим сумму
    console.log('Сумма: ' + sum);
}