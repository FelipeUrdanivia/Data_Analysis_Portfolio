import sqlite3
import pandas as pd

# Connect to the original SQLite database
conn_original = sqlite3.connect('sales_analysis.db')

# Load data from the 'products' and 'sales' tables into DataFrames
products_df = pd.read_sql_query("SELECT * FROM products;", conn_original)
sales_df = pd.read_sql_query("SELECT * FROM sales;", conn_original)

# Display an initial summary of the tables
print("Initial summary of products:")
print(products_df.info())
print("\nInitial summary of sales:")
print(sales_df.info())

# 1. Remove null values from the 'products' table
products_df = products_df.dropna(subset=['stock', 'price'], how='any')

# 2. Remove null values from the 'sales' table
sales_df = sales_df.dropna(subset=['quantity', 'total_amount', 'customer_name'], how='any')

# 3. Remove duplicates from both tables
products_df = products_df.drop_duplicates()
sales_df = sales_df.drop_duplicates()

# 4. Correct data types in the 'products' table
products_df['product_id'] = products_df['product_id'].astype(int)
products_df['price'] = products_df['price'].astype(float)
products_df['stock'] = products_df['stock'].astype(int)

# 5. Correct data types in the 'sales' table
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'], errors='coerce')  # 'coerce' converts errors to NaT
sales_df['total_amount'] = sales_df['total_amount'].astype(float)
sales_df['quantity'] = sales_df['quantity'].astype(int)

# 6. Normalize data
sales_df['customer_name'] = sales_df['customer_name'].str.lower()
sales_df['email'] = sales_df['email'].str.lower()

# 7. Display a final summary of the tables
print("\nFinal summary of products after cleaning:")
print(products_df.info())
print("\nFinal summary of sales after cleaning:")
print(sales_df.info())

# Create a new SQLite database for the cleaned data
conn_cleaned = sqlite3.connect('sales_analysis_cleaned.db')

# Save the cleaned DataFrames into new tables in the new database
products_df.to_sql('products', conn_cleaned, if_exists='replace', index=False)
sales_df.to_sql('sales', conn_cleaned, if_exists='replace', index=False)

# Confirmation that the data has been saved
print("\nCleaned data saved to the 'sales_analysis_cleaned.db' database.")

# Close both connections
conn_original.close()
conn_cleaned.close()
