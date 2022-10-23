import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='dummy'
)

cursor = connection.cursor()
delete_item_query = "DELETE FROM employee WHERE _id=2"

try:
    cursor.execute(delete_item_query)
    connection.commit()
    print("Delete user is successfully!!!")

except Exception as e:
    print(e)

connection.close()
