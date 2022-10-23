from unicodedata import name
from unittest import result
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    db="dummy"
)

cursor = connection.cursor()

select_query = "select * from employee"

try:
    cursor.execute(select_query)
    results = cursor.fetchall()
    for record in results:
        _id = record[0]
        name = record[1]
        print(f"ID is: {_id} and Name is: {name}")
    print("Query is successfully!!!")
except Exception as e:
    print(e)

connection.close()
