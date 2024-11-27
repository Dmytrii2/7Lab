import mysql.connector
from mysql.connector import Error

# Підключення до бази даних
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="mysql_db",
            user="user",
            password="password",
            database="phone_station"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Виконання SQL-запитів
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# SQL-запити для створення таблиць
create_clients_table = """
CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT,
    client_type VARCHAR(50),
    address VARCHAR(255),
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(100),
    PRIMARY KEY (client_id)
);
"""

create_phones_table = """
CREATE TABLE IF NOT EXISTS Phones (
    phone_number VARCHAR(15),
    client_id INT,
    PRIMARY KEY (phone_number),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);
"""

create_calls_table = """
CREATE TABLE IF NOT EXISTS Calls (
    call_id INT AUTO_INCREMENT,
    call_date DATE,
    phone_number VARCHAR(15),
    minutes INT,
    tariff_id INT,
    PRIMARY KEY (call_id),
    FOREIGN KEY (phone_number) REFERENCES Phones(phone_number),
    FOREIGN KEY (tariff_id) REFERENCES Tariffs(tariff_id)
);
"""

create_tariffs_table = """
CREATE TABLE IF NOT EXISTS Tariffs (
    tariff_id INT AUTO_INCREMENT,
    call_type VARCHAR(50),
    price_per_minute DECIMAL(5, 2),
    PRIMARY KEY (tariff_id)
);
"""

# Підключення до бази даних та створення таблиць
connection = create_connection()

if connection:
    execute_query(connection, create_clients_table)
    execute_query(connection, create_phones_table)
    execute_query(connection, create_calls_table)
    execute_query(connection, create_tariffs_table)
