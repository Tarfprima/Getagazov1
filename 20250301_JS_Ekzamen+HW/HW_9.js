let tbl; // это решил уже сделать глобальным переменным 

window.addEventListener('load', show)
// изначально сделал просто, чтобы при нажатии все окрашивалось в белый цвет, сливаясь с фоном (таким оброзом скрываясь)
// потом переделал через .display 
// вспомнил про .display из прошлых уроков в 24 году
// почитал про 'block' отсюда https://htmlbook.ru/css/display
// про 'none' знал
function show(){
    tbl = document.createElement('table');
    let tr = document.createElement('tr');
    tbl.appendChild(tr);
    let td = document.createElement('td');
    td.textContent = 'Пример таблицы';
    tr.appendChild(td);
    document.body.appendChild(tbl);
    tbl.style.display = 'none'; // Скрываем таблицу при загрузке 
    // .style в js изучали от 13 февраля там и подсмотрел кое что и дополнил 
}

function on() {
    tbl.style.display = 'block'; // появиться 
}

function off() {
    tbl.style.display = 'none'; // исчезнет
}

// долго решал эту задачу, переделал множество раз