import pymysql

# Config
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    db="dummy"
)
cursor = connection.cursor()

name_value = input("Enter your name: ")
insert_query_record = """INSERT INTO employee (name) VALUES ('%s')"""\
    %(name_value)

try:
    cursor.execute(insert_query_record)
    connection.commit()
except Exception as e:
    print(e)

connection.close()
