import pandas as pd
import sqlite3

# ------------------------------
# 1. Extract Excel
# ------------------------------

try:

    df_excel = pd.read_excel('data.xlsx')

    df_excel = df_excel.dropna(how='all')  # remove empty rows

    df_excel.reset_index(drop=True, inplace=True)

    print("Excel Data Preview:")

    print(df_excel.head())

except Exception as e:

    print("Error reading Excel:", e)

# ------------------------------
# 2. Simulate SQL Server
# ------------------------------

try:

    df_sql = pd.DataFrame({

        'EmpID': [1, 2, 3],

        'EmpName': ['John', 'Jane', 'Mike'],

        'Salary': [50000, 55000, 60000]

    })

    print("\nSimulated SQL Server Data Preview:")

    print(df_sql)

except Exception as e:

    print("Error simulating SQL Server:", e)

# ------------------------------
# 3. Create SQLite Database
# ------------------------------

try:

    conn = sqlite3.connect('etl_database.db')

    cursor = conn.cursor()

    # Create Project table
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Project (

            ID INTEGER,
            Name TEXT,
            Department TEXT,
            Salary REAL

        )

    ''')

    # Create Employee table
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Employee (

            EmpID INTEGER PRIMARY KEY,
            EmpName TEXT,
            Salary REAL

        )

    ''')

    # ------------------------------
    # 4. Load Data into Tables
    # ------------------------------

    df_excel.to_sql('Project', conn, if_exists='replace', index=False)

    df_sql.to_sql('Employee', conn, if_exists='replace', index=False)

    print("\nData loaded into SQLite database 'etl_database.db' successfully!")

except Exception as e:

    print("Error loading data into SQLite:", e)

# ------------------------------
# 5. Verify Data from Database
# ------------------------------

try:

    print("\nProject Data Preview:")

    project_data = pd.read_sql_query("SELECT * FROM Project LIMIT 5", conn)

    print(project_data)

    print("\nEmployee Data Preview:")

    employee_data = pd.read_sql_query("SELECT * FROM Employee", conn)

    print(employee_data)

    conn.close()

except Exception as e:

    print("Error reading data from SQLite:", e)