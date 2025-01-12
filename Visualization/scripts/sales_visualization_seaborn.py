import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Connect to the database
conn = sqlite3.connect('../visualization_data.db')  # Relative path to your database

# 2. Query to get total sales by month and category
query = """
SELECT 
    strftime('%Y-%m', sale_date) AS month,
    SUM(total_amount) AS total_sales,
    p.category
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY month, p.category
ORDER BY month;
"""

# Load the data into a DataFrame
df_sales = pd.read_sql_query(query, conn)

# 3. Close the connection to the database
conn.close()

# 4. Visualization with Seaborn
# Set up style for a clean and attractive visualization
sns.set(style="whitegrid")

# Create a figure for the plot
plt.figure(figsize=(14, 7))

# Line plot for total sales by month and category
sns.lineplot(data=df_sales, x='month', y='total_sales', hue='category', marker='o', palette='tab10')

# Customize the plot
plt.title('Total Sales by Month and Category', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.legend(title='Category')

# Adjust layout to ensure everything looks good
plt.tight_layout()

# Show the plot
plt.show()
