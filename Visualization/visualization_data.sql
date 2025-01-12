-- Create database schema

-- Drop tables if they already exist to avoid duplication
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS campaigns;

-- Create products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);

-- Create campaigns table
CREATE TABLE campaigns (
    campaign_id INTEGER PRIMARY KEY,
    campaign_name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL
);

-- Create sales table
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    campaign_id INTEGER,
    sale_date TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (product_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns (campaign_id)
);

-- Insert data into products
INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Product A', 'Category 1', 10.0),
(2, 'Product B', 'Category 1', 15.0),
(3, 'Product C', 'Category 2', 20.0),
(4, 'Product D', 'Category 2', 25.0),
(5, 'Product E', 'Category 3', 30.0),
(6, 'Product F', 'Category 3', 35.0);

-- Insert data into campaigns
INSERT INTO campaigns (campaign_id, campaign_name, start_date, end_date) VALUES
(1, 'Winter Sale', '2022-01-01', '2022-01-31'),
(2, 'Spring Promotion', '2022-03-01', '2022-03-31'),
(3, 'Summer Sale', '2022-06-01', '2022-06-30'),
(4, 'Autumn Discount', '2022-09-01', '2022-09-30'),
(5, 'Holiday Specials', '2022-12-01', '2022-12-31');

-- Insert data into sales
INSERT INTO sales (sale_id, product_id, campaign_id, sale_date, quantity, total_amount) VALUES
(1, 1, 1, '2022-01-05', 10, 100.0),
(2, 2, 1, '2022-01-15', 5, 75.0),
(3, 3, 2, '2022-03-10', 8, 160.0),
(4, 4, 2, '2022-03-20', 4, 100.0),
(5, 5, 3, '2022-06-05', 12, 360.0),
(6, 6, 3, '2022-06-18', 6, 210.0),
(7, 1, 4, '2022-09-03', 9, 90.0),
(8, 2, 4, '2022-09-15', 7, 105.0),
(9, 3, 5, '2022-12-02', 15, 300.0),
(10, 4, 5, '2022-12-18', 5, 125.0),
(11, 5, 2, '2022-03-25', 10, 300.0),
(12, 6, 4, '2022-09-20', 8, 280.0),
(13, 1, 5, '2022-12-22', 20, 200.0),
(14, 2, 3, '2022-06-25', 10, 150.0),
(15, 3, 1, '2022-01-28', 6, 120.0);
