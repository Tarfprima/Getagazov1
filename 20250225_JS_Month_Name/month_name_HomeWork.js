function create_season_table() {
    // Создаем таблицу
    const tbl = document.createElement('table');
    document.body.appendChild(tbl);

    // Первая строка: заголовки сезонов
    let tr = document.createElement('tr');
    tbl.appendChild(tr);

    let td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Весна";
    td.style.backgroundColor = 'lightgreen'; // Фон для весны

    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Лето";
    td.style.backgroundColor = 'yellow'; // Фон для лета

    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Осень";
    td.style.backgroundColor = 'orange'; // Фон для осени

    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "Зима";
    td.style.backgroundColor = 'lightblue'; // Фон для зимы

    // Вторая строка: месяцы для каждого сезона
    tr = document.createElement('tr');
    tbl.appendChild(tr);

    // Весна: март, апрель, май
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "март, апрель, май";
    td.style.backgroundColor = 'lightgreen';

    // Лето: июнь, июль, август
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "июнь, июль, август";
    td.style.backgroundColor = 'yellow';

    // Осень: сентябрь, октябрь, ноябрь
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "сентябрь, октябрь, ноябрь";
    td.style.backgroundColor = 'orange';

    // Зима: декабрь, январь, февраль
    td = document.createElement('td');
    tr.appendChild(td);
    td.textContent = "декабрь, январь, февраль";
    td.style.backgroundColor = 'lightblue';
}

// Запускаем функцию после загрузки страницы
window.addEventListener('load', create_season_table);