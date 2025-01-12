-- Creación de tablas
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    sale_date TEXT,
    quantity INTEGER,
    total_amount REAL,
    customer_name TEXT,
    email TEXT,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

-- Insertar datos sucios en la tabla de productos
INSERT INTO products (product_id, product_name, category, price, stock) VALUES
(1, 'Laptop', 'Electronics', 999.99, 15),
(2, 'Smartphone', 'Electronics', 499.99, 30),
(3, 'Tablet', 'Electronics', 349.99, NULL), -- stock vacío
(4, 'Headphones', 'Electronics', 149.99, 50),
(5, 'Coffee Maker', 'Home Appliances', 89.99, 20),
(6, 'Microwave', 'Home Appliances', NULL, 10), -- precio nulo
(7, 'Blender', 'Home Appliances', 120.50, 25),
(8, 'Coffee Maker', 'Home Appliances', 89.99, 20); -- duplicado

-- Insertar datos sucios en la tabla de ventas
INSERT INTO sales (sale_id, product_id, sale_date, quantity, total_amount, customer_name, email) VALUES
(1, 1, '2024-01-01', 2, 1999.98, 'John Doe', 'john.doe@example.com'),
(2, 3, '2024-01-02', 1, 349.99, 'Jane Smith', 'jane.smith@example.com'),
(3, 2, '2024-01-03', 3, 1499.97, 'Alice Johnson', 'alice.johnson@example.com'),
(4, 4, '2024-01-04', 5, 749.95, 'Chris Lee', 'chris.lee@example.com'),
(5, 5, '2024-01-05', NULL, NULL, 'Bob Brown', 'bob.brown@example.com'), -- datos nulos
(6, 6, '2024-02-01', 1, 89.99, 'Mary White', 'mary.white@example.com'),
(7, 7, '2024-02-02', 2, 241.00, 'James Black', 'james.black@example.com'),
(8, 8, '2024-02-03', 1, 89.99, 'Anna Blue', 'anna.blue@example.com'),
(9, 5, '2024-02-04', 1, 89.99, 'Olivia Green', 'olivia.green@example.com'),
(10, 2, '2024-03-01', 3, 1499.97, 'Sophia Pink', 'sophia.pink@example.com');
