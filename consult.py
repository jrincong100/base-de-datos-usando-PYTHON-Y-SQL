import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        db='mi_db_1'
    )

cursor=connection.cursor()


cursor.execute("SELECT Employee_ID, Full_Name, Job_Title, Age " \
"FROM data1 LIMIT 5")


for fila in cursor.fetchall():
    print(fila)

cursor.commit()
cursor.close()