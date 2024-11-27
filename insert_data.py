import psycopg2

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="phone_station", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

# Вставка даних для клієнтів
cursor.execute("INSERT INTO Clients (client_type, address, last_name, first_name, patronymic) VALUES (%s, %s, %s, %s, %s)",
               ('фізична особа', 'вул. Лесі Українки, 1', 'Іваненко', 'Іван', 'Іванович'))

# Вставка телефонів
cursor.execute("INSERT INTO Phones (phone_number, client_id) VALUES (%s, %s)", ('0501234567', 1))

# Вставка тарифів
cursor.execute("INSERT INTO Tariffs (call_type, cost_per_minute) VALUES (%s, %s)",
               ('міжміський', 0.5))

# Вставка розмов
cursor.execute("INSERT INTO Calls (call_date, phone_number, duration, tariff_id) VALUES (%s, %s, %s, %s)",
               ('2024-11-01', '0501234567', 10, 1))

# Збереження змін
conn.commit()
cursor.close()
conn.close()
