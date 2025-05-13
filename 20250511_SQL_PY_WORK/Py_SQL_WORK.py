import psycopg

# Подключение к базе данных (замените параметры на свои)
conn = psycopg.connect(
    dbname='students',
    user='getag',

)
cur = conn.cursor()

# Получаем категории
cur.execute("SELECT id, name FROM categories")
categories = {row[0]: row[1] for row in cur.fetchall()}

# Получаем дела
cur.execute("SELECT category_id, start_time, end_time FROM activities")
activities = cur.fetchall()

# Вычисляем время по категориям
category_times = {cat_id: 0 for cat_id in categories}
total_time = 0

for activity in activities:
    cat_id, start, end = activity
    duration = (end - start).total_seconds() / 3600  # Переводим в часы
    category_times[cat_id] += duration
    total_time += duration

# Закрываем соединение
cur.close()
conn.close()