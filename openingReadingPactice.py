import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('chinook.db')

# Execute a SQL query
customer_query = 'SELECT * FROM customers;'
customer_table = pd.read_sql_query(customer_query, conn)

# Print the results
print(customer_table)

# Close the connection
conn.close()