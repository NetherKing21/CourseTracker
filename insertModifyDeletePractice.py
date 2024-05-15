import sqlite3
import pandas as pd

# Set up
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

# Beforehand preview showing the last 5 rows
preview = 'SELECT * FROM (SELECT * FROM genres ORDER BY GenreId DESC LIMIT 5) ORDER BY GenreID ASC;'
print(pd.read_sql_query(preview, conn))

# Adding insert and viewing it
insert_query = "INSERT INTO genres VALUES (26, 'Garbage');"
cursor.execute(insert_query)
conn.commit()

after_insert = 'SELECT * FROM (SELECT * FROM genres ORDER BY GenreId DESC LIMIT 5) ORDER BY GenreID ASC;'
print(pd.read_sql_query(after_insert, conn))

# Modify result and view it
modify_query = "UPDATE genres SET Name = 'Not Garbage' WHERE GenreId = 26;"
cursor.execute(modify_query)
conn.commit()

after_modify = 'SELECT * FROM (SELECT * FROM genres ORDER BY GenreId DESC LIMIT 5) ORDER BY GenreID ASC;'
print(pd.read_sql_query(after_modify, conn))

# Delete new row and view it
delete_query = "DELETE FROM genres WHERE GenreId = 26;"
cursor.execute(delete_query)
# conn.commit()

after_delete = 'SELECT * FROM (SELECT * FROM genres ORDER BY GenreId DESC LIMIT 5) ORDER BY GenreID ASC;'
print(pd.read_sql_query(after_delete, conn))


# Close Connection!!!
conn.close()