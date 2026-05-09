import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('etl_database.db')

# View Project Table
df_project = pd.read_sql_query("SELECT * FROM Project", conn)
print("Project Data:")
print(df_project.head())

# View Employee Table
df_employee = pd.read_sql_query("SELECT * FROM Employee", conn)
print("\nEmployee Data:")
print(df_employee.head())

conn.close()