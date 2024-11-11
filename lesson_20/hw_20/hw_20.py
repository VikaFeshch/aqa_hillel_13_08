import sqlite3

# Підключення до бази даних (якщо файлу бази немає, він буде створений)
conn = sqlite3.connect('internet_store')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
    )
''')

# Додавання даних у таблицю categories
cursor.executemany('''
    INSERT INTO categories (category_name) VALUES (?)
''', [
    ('Electronics',),
    ('Books',),
    ('Clothing',)
])

# Додавання даних у таблицю products
cursor.executemany('''
    INSERT INTO products (product_name, description, price, category_id) VALUES (?, ?, ?, ?)
''', [
    ('Smartphone', 'Latest model smartphone with high-resolution camera', 699.99, 1),
    ('Laptop', 'Lightweight laptop with 16GB RAM and 512GB SSD', 1200.00, 1),
    ('Novel', 'A best-selling novel', 15.99, 2),
    ('T-shirt', 'Comfortable cotton T-shirt', 9.99, 3)
])

conn.commit()  # Збереження змін у базі даних

# JOIN-запит для виведення даних
cursor.execute('''
    SELECT products.product_name, products.description, products.price, categories.category_name
    FROM products
    JOIN categories ON products.category_id = categories.category_id
''')

# Виведення результатів запиту
for row in cursor.fetchall():
    print(row)

# Закриття з'єднання
conn.close()
