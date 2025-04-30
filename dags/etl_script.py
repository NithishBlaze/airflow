import csv
from datetime import datetime
from os.path import exists

import pyodbc
import os

now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")


def database_connection():
    server = '301224HP840G545'
    database = 'UserData'
    connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database}; Trusted_Connection=yes;')
    cursor = connection.cursor()
    connection.commit()

    cursor.execute('SELECT * from Users')

    datas = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    print(datas)

    cursor.close()
    connection.close()

    return columns, datas

def write_to_file(columns, datas):
    # filepath = "/home/nithishkumar/airflow_output"
    filepath = "C:\\Users\\nithishkumar.r\Desktop\Output"

    os.makedirs(filepath, exist_ok = True)

    filename = os.path.join(filepath, f"user_data {date_time}.csv")
    with open(filename,'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(datas)

    print(f"Data written to: {filename}")
def process():
    columns, datas = database_connection()
    write_to_file(columns, datas)

if __name__ == "__main__":
    process()

