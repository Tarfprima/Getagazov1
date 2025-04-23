-- Создаём таблицу для книг

CREATE TABLE books (
    title VARCHAR(100),         -- Название
    author_surname VARCHAR(50), -- Фамилия автора
    author_name VARCHAR(50),    -- Имя автора
    year INTEGER,               -- Год издания
    number VARCHAR(16),         -- Номер 
    periodicity VARCHAR(16)     -- периодичность
);


-- Добавляем записи: книги и журналы
INSERT INTO books (title, author_surname, author_name, year, number, periodicity) VALUES
    ('Война и мир', 'Толстой', 'Лев', 1865, '12345', NULL),          -- Книга
    ('Преступление и наказание', 'Достоевский', 'Фёдор', 1866, '67890', NULL),  -- Книга
    ('Гарри Поттер', 'Роулинг', 'Дж. К.', 1997, '54321', NULL),      -- Книга
    ('Журнал "Комиксы"', 'Стэн', 'Ли', 2025, '11', 'месяц'),   -- Журнал
    ('Журнал "Комиксы"', 'Стэн', 'Ли', 2025, '12', 'месяц');   -- Журнал

-- искать записи с определённой периодичностью.
SELECT * FROM books WHERE periodicity = 'месяц';

-- Если нужно изменить периодичность, надо использовать UPDATE

UPDATE books SET periodicity = 'неделя' WHERE title = 'Журнал "Комиксы"';




-- БЕЗ КОММЕНТОВ для вставки в консоль

CREATE TABLE books (
    title VARCHAR(100),         
    author_surname VARCHAR(50), 
    author_name VARCHAR(50),    
    year INTEGER,               
    number VARCHAR(16),         
    periodicity VARCHAR(16)     
);

INSERT INTO books (title, author_surname, author_name, year, number, periodicity) VALUES
    ('Война и мир', 'Толстой', 'Лев', 1865, '12345', NULL),          
    ('Преступление и наказание', 'Достоевский', 'Фёдор', 1866, '67890', NULL),  
    ('Гарри Поттер', 'Роулинг', 'Дж. К.', 1997, '54321', NULL),      
    ('Журнал "Комиксы"', 'Стэн', 'Ли', 2025, '11', 'месяц'),   
    ('Журнал "Комиксы"', 'Стэн', 'Ли', 2025, '12', 'месяц');  