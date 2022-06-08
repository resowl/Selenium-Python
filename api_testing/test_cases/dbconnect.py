import mysql.connector as mysqlconn

conn = mysqlconn.connect(host='localhost', user='root', passwd='root', database= 'priya')
if conn.is_connected():
    print("connection is successful************")

cursor = conn.cursor()

query = "Insert into priyaemp values(1, 'abcde', 5000)"
cursor.execute(query)
conn.commit()
print("Data inserted successfully")