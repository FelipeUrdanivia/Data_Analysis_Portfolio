-- Creación de tablas
CREATE TABLE IF NOT EXISTS campaigns (
    campaign_id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    budget DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (campaign_id) REFERENCES campaigns (campaign_id),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE IF NOT EXISTS channels (
    channel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel_name TEXT NOT NULL,
    platform TEXT NOT NULL
);

-- Inserción de datos en campaigns
INSERT INTO campaigns (campaign_name, start_date, end_date, budget) VALUES
('Summer Sale', '2024-06-01', '2024-06-30', 10000.00),
('Winter Discount', '2024-12-01', '2024-12-31', 8000.00),
('Valentine''s Day Offer', '2024-02-01', '2024-02-14', 7000.00),
('Spring Clearance', '2024-03-01', '2024-03-31', 12000.00),
('Black Friday Special', '2024-11-01', '2024-11-29', 15000.00),
('Cyber Monday Deals', '2024-11-30', '2024-12-07', 13000.00),
('Christmas Sale', '2024-12-01', '2024-12-25', 20000.00),
('New Year Promo', '2024-12-26', '2025-01-01', 9000.00),
('Easter Discount', '2024-04-01', '2024-04-10', 4000.00),
('Summer Flash Sale', '2024-06-01', '2024-06-07', 6000.00),
('Autumn Bonanza', '2024-09-01', '2024-09-30', 9500.00),
('Black Friday Deals', '2024-11-01', '2024-11-29', 18000.00),
('Winter Wonderland', '2024-12-01', '2024-12-15', 11000.00);

-- Inserción de datos en customers
INSERT INTO customers (name, email, age, location) VALUES
('Alice', 'alice_new@example.com', 30, 'Berlin'),
('Bob', 'bob_new@example.com', 25, 'Hamburg'),
('Charlie', 'charlie@example.com', 35, 'Munich'),
('David', 'david@example.com', 40, 'Cologne'),
('Eva', 'eva@example.com', 28, 'Berlin'),
('Frank', 'frank_new@example.com', 50, 'Stuttgart'),
('Grace', 'grace@example.com', 22, 'Düsseldorf'),
('Helen', 'helen@example.com', 32, 'Leipzig'),
('Iris', 'iris@example.com', 27, 'Hamburg'),
('James', 'james@example.com', 36, 'Frankfurt');

-- Inserción de datos en channels
INSERT INTO channels (channel_name, platform) VALUES
('Social Media', 'Facebook'),
('Email Campaign', 'MailChimp'),
('Search Ads', 'Google'),
('Display Ads', 'Google'),
('Affiliate Marketing', 'Rakuten'),
('Influencer Marketing', 'Instagram'),
('TV Ads', 'RTL'),
('YouTube Ads', 'YouTube'),
('Radio Ads', 'Spotify'),
('Event Sponsorship', 'Local Events');

-- Inserción de datos en sales
INSERT INTO sales (campaign_id, customer_id, sale_date, amount) VALUES
(1, 1, '2024-06-15', 200.00),
(1, 2, '2024-06-18', 300.00),
(2, 3, '2024-12-10', 150.00),
(2, 4, '2024-12-15', 250.00),
(3, 5, '2024-02-05', 400.00),
(4, 6, '2024-03-10', 500.00),
(4, 7, '2024-03-20', 450.00),
(5, 8, '2024-11-05', 1200.00),
(6, 9, '2024-12-01', 800.00),
(7, 10, '2024-12-10', 1000.00),
(8, 1, '2024-12-26', 700.00),
(9, 2, '2024-04-02', 350.00),
(10, 3, '2024-06-02', 450.00);
