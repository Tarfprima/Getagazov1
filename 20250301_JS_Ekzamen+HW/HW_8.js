window.addEventListener('load', first)

function first(){

    let tbl = document.createElement('table');
    document.body.appendChild(tbl);

    let tr = document.createElement('tr');
    tbl.appendChild(tr);

    // Цикл for от 1 до 10:
    // Создает ячейку (<td>)
    // Записывает в ячейку квадрат числа (i * i) через textContent.
    // Добавляет ячейку в строку через appendChild.
    // Простое условие, но было не легко

    for (let i = 1; i <= 10; i++){
        let td = document.createElement('td');
        td.textContent = i * i;
        tr.appendChild(td);
    }
}