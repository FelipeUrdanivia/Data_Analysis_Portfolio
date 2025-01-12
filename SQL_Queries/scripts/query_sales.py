import sqlite3
import pandas as pd

# Conectarse a la base de datos
conn = sqlite3.connect('marketing.db')

# Crear un archivo HTML con el encabezado
html_content = """
<html>
<head>
    <title>Sales Reports</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 8px 12px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Sales Reports</h1>
"""

# Query 1: Total Sales by Campaign
query_campaign_sales = """
SELECT c.campaign_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN campaigns c ON s.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
"""
df_campaign_sales = pd.read_sql_query(query_campaign_sales, conn)
html_content += "<h2>Total Sales by Campaign</h2>" + df_campaign_sales.to_html(index=False)

# Query 2: Total Sales by Customer
query_customer_sales = """
SELECT cu.name AS customer_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN customers cu ON s.customer_id = cu.customer_id
GROUP BY cu.name
ORDER BY total_sales DESC;
"""
df_customer_sales = pd.read_sql_query(query_customer_sales, conn)
html_content += "<h2>Total Sales by Customer</h2>" + df_customer_sales.to_html(index=False)

# Query 3: Total Sales by Channel
query_channel_sales = """
SELECT ch.channel_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN campaigns c ON s.campaign_id = c.campaign_id
JOIN channels ch ON c.campaign_id = ch.channel_id
GROUP BY ch.channel_name
ORDER BY total_sales DESC;
"""
df_channel_sales = pd.read_sql_query(query_channel_sales, conn)
html_content += "<h2>Total Sales by Channel</h2>" + df_channel_sales.to_html(index=False)

# Query 4: Sales by Date
query_sales_by_date = """
SELECT sale_date, SUM(amount) AS total_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
"""
df_sales_by_date = pd.read_sql_query(query_sales_by_date, conn)
html_content += "<h2>Sales by Date</h2>" + df_sales_by_date.to_html(index=False)

# Query 5: Customers by Location
query_customers_by_location = """
SELECT location, COUNT(*) AS customer_count
FROM customers
GROUP BY location;
"""
df_customers_by_location = pd.read_sql_query(query_customers_by_location, conn)
html_content += "<h2>Customers by Location</h2>" + df_customers_by_location.to_html(index=False)

# Query 6: Sales by Campaign and Customer
query_sales_by_campaign_customer = """
SELECT c.campaign_name, cu.name AS customer_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN campaigns c ON s.campaign_id = c.campaign_id
JOIN customers cu ON s.customer_id = cu.customer_id
GROUP BY c.campaign_name, cu.name
ORDER BY c.campaign_name, total_sales DESC;
"""
df_sales_by_campaign_customer = pd.read_sql_query(query_sales_by_campaign_customer, conn)
html_content += "<h2>Sales by Campaign and Customer</h2>" + df_sales_by_campaign_customer.to_html(index=False)

# Query 7: Top 5 Campaigns with the Most Sales
query_top_campaigns = """
SELECT c.campaign_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN campaigns c ON s.campaign_id = c.campaign_id
GROUP BY c.campaign_name
ORDER BY total_sales DESC
LIMIT 5;
"""
df_top_campaigns = pd.read_sql_query(query_top_campaigns, conn)
html_content += "<h2>Top 5 Campaigns with the Most Sales</h2>" + df_top_campaigns.to_html(index=False)

# Query 8: Sales by Channel (counting the number of sales)
query_sales_count_by_channel = """
SELECT ch.channel_name, COUNT(s.sale_id) AS total_sales
FROM sales s
JOIN campaigns c ON s.campaign_id = c.campaign_id
JOIN channels ch ON c.campaign_id = ch.channel_id
GROUP BY ch.channel_name
ORDER BY total_sales DESC;
"""
df_sales_count_by_channel = pd.read_sql_query(query_sales_count_by_channel, conn)
html_content += "<h2>Number of Sales by Channel</h2>" + df_sales_count_by_channel.to_html(index=False)

# Query 9: Total Sales by Campaign with Min and Max Sale Amount
query_sales_min_max = """
SELECT c.campaign_name, 
       MIN(s.amount) AS min_sale, 
       MAX(s.amount) AS max_sale, 
       SUM(s.amount) AS total_sales
FROM sales s
JOIN campaigns c ON s.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
"""
df_sales_min_max = pd.read_sql_query(query_sales_min_max, conn)
html_content += "<h2>Total Sales by Campaign with Min and Max Sale Amount</h2>" + df_sales_min_max.to_html(index=False)

# Cerrar la base de datos
conn.close()

# Cerrar el archivo HTML
html_content += """
</body>
</html>
"""

# Guardar todo en un solo archivo HTML
with open('all_sales_reports.html', 'w') as f:
    f.write(html_content)

print("The HTML file with all reports has been generated.")
