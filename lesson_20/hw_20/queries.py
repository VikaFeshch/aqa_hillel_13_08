# -- Створення таблиці categories
# CREATE TABLE categories (
#     category_id SERIAL PRIMARY KEY,
#     category_name VARCHAR(50) NOT NULL
# );
# #
# -- Створення таблиці products з зовнішнім ключем на categories
# CREATE TABLE products (
#     product_id SERIAL PRIMARY KEY,
#     product_name VARCHAR(100) NOT NULL,
#     description TEXT,
#     price DECIMAL(10, 2) NOT NULL,
#     category_id INT REFERENCES categories(category_id)
# );
#
#
# -- Вставка даних у таблицю categories
# INSERT INTO categories (category_name) VALUES
# ('Auto & moto'),
# ('Instrument'),
# ('Accessory');
#
# -- Вставка даних у таблицю products
# INSERT INTO products (product_name, description, price, category_id) VALUES
# ('Battery', 'Moto battery for Scooter 4A 12V YAMAHA/SUZUKI', 3699.99, 1),
# ('Battery charger', 'Volt Polska SMART A16 15 Amp 12V battery charger', 1200.00, 1),
# ('Jack', 'Diamond-shaped jack with ratchet 2 t Heyner UltraLift', 1119.99, 2),
# ('Bag organizer', 'Bag organizer in the trunk of the car', 9.99, 3);
#
#
# SELECT products.product_name as Products, products.description as Description, products.price as Price,
# categories.category_name as Category
# FROM products
# JOIN categories ON products.category_id = categories.category_id;
