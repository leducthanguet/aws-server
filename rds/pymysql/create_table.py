
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    db="dummy"
)

cursor = connection.cursor()
delete_existing_table = "drop table if exists employee";
create_table_query = """create table employee(
_id int auto_increment primary key,
name varchar(20) not null
)"""

try:
    cursor.execute(delete_existing_table)
    print("Existing table has been deleted")
    cursor.execute(create_table_query)
    print("Employ Table has been created!")
except Exception as e:
    print(f"Exception is: {e}")

connection.close()
