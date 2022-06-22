import mysql.connector

class Database_Class_Page:
    def connect_to_database(self, host, user, password, database):
        connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database="prjay")
        if connection.is_connected():
            print("connection is successful************")
        return connection

    def execute_a_query(self, connection, query_to_execute):
        cursor = connection.cursor()
        query = query_to_execute
        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()
        print(cursor.rowcount, "rows printed")
        print("Query executed successfully********")

    def execute_multiple_queries(self, connection, queries_to_execute, value):
        cursor = connection.cursor()
        query = queries_to_execute
        try:
            cursor.executemany(query, value) #value is list of tuples
            connection.commit()
        except:
            connection.rollback()
        print(cursor.rowcount, "rows printed")
        print("Queries executed successfully********")

    def fetch_all_records(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            records = cursor.fetchall()
            print(records)
            for record in records:
                print(record)
                return (record)
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()


    def fetch_only_one_record(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            record = cursor.fetchone()
            print(record)
            for entry in record:
                print(entry)
                return (entry)
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()






'''
# query = "create database pshah"
# query = "create table st1(rollnum int not null primary key, sname varchar(10) not null, branch varchar(10) not null)"
# query = "insert into st1(rollnum, sname, branch) values (%s, %s, %s)"
# value= [(103,"jaymin", "ITtech"), (102,"neha", "mba"), (104,"jacob", "test eng")]
# query = "alter table st1 add section varchar(10) default 'A'"
'''
