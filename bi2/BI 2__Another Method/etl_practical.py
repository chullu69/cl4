import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# ------------------------------

# 1. Extract Excel (skip metadata rows)

# ------------------------------

try:

    df_excel = pd.read_excel('data.xlsx')

    df_excel.reset_index(drop=True, inplace=True)

    # Fill missing Progress values

    if 'Progress' in df_excel.columns:

        df_excel['Progress'] = df_excel['Progress'].fillna(0)

    print("Excel Data Preview:")

    print(df_excel.head())

except Exception as e:

    print("Error reading Excel:", e)

# ------------------------------

# 2. Simulate SQL Server

# ------------------------------

df_sql = pd.DataFrame({

    'EmpID': [1, 2, 3],

    'EmpName': ['John', 'Jane', 'Mike'],

    'Salary': [50000, 55000, 60000]

})

print("\nSimulated SQL Server Data Preview:")

print(df_sql)

# ------------------------------

# 3. SQL Salary Stats

# ------------------------------

salary_stats = df_sql['Salary'].describe()

print("\nSalary Stats from SQL Data:")

print(salary_stats)

# ------------------------------

# 4. Visualization

# ------------------------------

try:

    # SQL Data: Employee Salary Bar Chart

    plt.figure(figsize=(6,4))

    sns.barplot(x='EmpName', y='Salary', data=df_sql, palette="magma")

    plt.title('Employee Salary (Simulated SQL Data)')

    plt.ylabel('Salary')

    plt.xlabel('Employee Name')

    plt.tight_layout()

    plt.savefig('sql_salary_chart.png')

    plt.close()

    # Excel Data: Days Required per Project Horizontal Bar Chart

    if 'Name' in df_excel.columns and 'Salary' in df_excel.columns:

        plt.figure(figsize=(10,5))

        sns.barplot(y='Salary', x='Name', data=df_excel, palette='viridis')

        plt.title('Employee Salary from Excel Data')

        plt.xlabel('Employee Name')

        plt.ylabel('Salary')

        plt.tight_layout()

        plt.savefig('excel_salary_chart.png')

        plt.close()

    # ETL Data Source Distribution Pie Chart

    etl_data = [len(df_excel), len(df_sql)]

    labels = ['Excel Rows', 'SQL Rows']

    plt.figure(figsize=(5,5))

    plt.pie(etl_data, labels=labels, autopct='%1.1f%%', colors=['skyblue','orange'])

    plt.title('ETL Data Source Distribution')

    plt.savefig('etl_distribution_chart.png')

    plt.close()

except Exception as e:

    print("Error creating visualizations:", e)

# ------------------------------

# 5. Load to Target Excel

# ------------------------------

try:

    with pd.ExcelWriter('etl_target_data.xlsx') as writer:

        df_excel.to_excel(writer, sheet_name='Excel_Data', index=False)

        df_sql.to_excel(writer, sheet_name='SQL_Data', index=False)

    print("\nETL Practical Completed Successfully!")

    print("Charts saved as PNG and data in etl_target_data.xlsx")

except Exception as e:

    print("Error saving target data:", e)