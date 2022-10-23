import pymysql

connection =  pymysql.connect(
        host='localhost',
        user='root', 
        password = "password",
        db='dummy',
        )

cursor = connection.cursor()
sql_query = "SELECT VERSION()"

try:
    cursor.execute(sql_query)
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print(e)
connection.close()
