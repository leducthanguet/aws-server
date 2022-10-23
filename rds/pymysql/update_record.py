import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    db="dummy"
)

new_name = "Le Duc Chien"

cursor = connection.cursor()
update_query = """UPDATE employee
SET name=('%s')
WHERE _id=1
"""\
%(new_name)

try:
    cursor.execute(update_query)
    connection.commit()
    print("Update is successfully!!!")

except Exception as e:
    print(e)

connection.close()
