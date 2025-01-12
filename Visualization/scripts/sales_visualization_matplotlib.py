import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the database
conn = sqlite3.connect('../visualization_data.db')  # Go up one level to access the database

# 2. Query for sales by month
query = """
SELECT 
    strftime('%Y-%m', sale_date) AS month,
    SUM(total_amount) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;
"""

# Load the query results into a DataFrame
df_sales = pd.read_sql_query(query, conn)

# 3. Close the database connection
conn.close()

# 4. Visualization with Matplotlib
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(df_sales['month'], df_sales['total_sales'], marker='o', linestyle='-', color='green')

# Customize the chart
plt.title('Total Sales Over Time', fontsize=14)  # Set the title
plt.xlabel('Month', fontsize=12)  # Set the x-axis label
plt.ylabel('Total Sales ($)', fontsize=12)  # Set the y-axis label
plt.grid(True)  # Display the grid
plt.xticks(rotation=45)  # Rotate the x-axis labels for better visibility

# Adjust the layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()
