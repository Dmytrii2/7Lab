import psycopg2

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="phone_station", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

# Виведення всіх таблиць і їх даних
tables = ['Clients', 'Phones', 'Calls', 'Tariffs']
for table in tables:
    print(f"Таблиця {table}:")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()

cursor.close()
conn.close()
