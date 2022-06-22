import mysql.connector

class Db_Class_Page:
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
            # cursor.executemany(query, value)
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



'''
# query = "create database pshah"
# query = "create table st1(rollnum int not null primary key, sname varchar(10) not null, branch varchar(10) not null)"
# query = "insert into st1(rollnum, sname, branch) values (%s, %s, %s)"
# value= [(103,"jaymin", "ITtech"), (102,"neha", "mba"), (104,"jacob", "test eng")]
# query = "alter table st1 add section varchar(10) default 'A'"
'''
