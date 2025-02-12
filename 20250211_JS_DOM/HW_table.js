
function main_func() {
    console.log('Страница готова к работе');
    add_table_to_page(create_addition_table()); // Используем новую функцию для создания таблицы сложения
}

function add_table_to_page(tbl) {
    // Функция добавляет таблицу в тело страницы
    document.body.appendChild(tbl);
}

function create_addition_table() {
    // Создадим таблицу сложения
    let result = document.createElement('table');  // Создаем элемент таблицы

    let tr;
    let td;
    for (let rowi = 0; rowi < 10; rowi++) {
        // Создаем строку таблицы
        tr = document.createElement('tr');
        result.appendChild(tr);  // Добавляем строку в таблицу

        for (let coli = 0; coli < 10; coli++) {
            // Создаем ячейку таблицы
            td = document.createElement('td');
            tr.appendChild(td);  // Добавляем ячейку в строку

            // Заполняем ячейку суммой индексов строки и столбца
            td.textContent = rowi + coli;
        }
    }

    return result;  // Возвращаем готовую таблицу
}

window.addEventListener(
    'load',
    main_func  // Вызываем главную функцию при загрузке страницы
);
