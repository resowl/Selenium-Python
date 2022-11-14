import mysql.connector
from database import python_mysql_dbconfig
from mysql.connector import MySQLConnection, Error
import json
from abc import ABC, abstractmethod

class Database_Class(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_a_query(self, query_to_execute):
        pass

    @abstractmethod
    def execute_multiple_queries(self, queries_to_execute, value):
        pass

    @abstractmethod
    def fetch_records(self, query):
        pass

class mysql_connect(Database_Class):
    def connect(self):
        try:
            db_config = python_mysql_dbconfig.read_db_config()
            conn = None
            print("Connecting to MySQL database...")
            conn = MySQLConnection(**db_config)
            if conn.is_connected():
                db_Info = conn.get_server_info()
                print("Connected to MySQL Server version:--> ", db_Info)
                print("Connection established.")
                return conn
        except Error as e:
            print("Error while connecting to MySQL", e)


    def execute_a_query(self, query_to_execute):
        connection = self.connect()
        cursor = connection.cursor()
        # global connection timeout arguments
        '''global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)'''

        #query_to_execute = "create database abcdefg"
        try:
            cursor.execute(query_to_execute)
            connection.commit()
        except:
            connection.rollback()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        print(cursor.rowcount, "rows printed")
        print("Query executed successfully********")

    def execute_multiple_queries(self, queries_to_execute, value):
        connection = self.connect()
        cursor = connection.cursor()
        try:
            result_iterator = cursor.execute(queries_to_execute, value) #value is list of tuples
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query
                print(f"Affected {res.rowcount} rows")
            connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
        print(cursor.rowcount, "rows printed")
        print("Queries executed successfully********")

    def fetch_all_records(self, query):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            fetch_result = cursor.fetchall()
            print(json.dumps(fetch_result, indent=4))
            all_records = []
            for record in fetch_result:
                if record!= None:
                    all_records.append(record)

            print(all_records)
            return all_records
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()

    def fetch_only_one_record(self, query):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            fetch_result = cursor.fetchone()
            print("Json Format:-->", json.dumps(fetch_result, indent=4))
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()

    def fetch_records(self, query):
        print("Into fetch_records implementation")


m = mysql_connect()
m.connect()
# d.execute_a_query()
# d.execute_a_query("create table student123(rollnum int not null primary key, sname varchar(10) not null, branch varchar(10) not null)")
data_to_insert = "[(106, 'vedant', 'grade8'),(107, 'apurv', 'grade9'),(108, 'vanshi', 'grade10')]"
query = "insert into student123(rollnum, sname, branch) values (%s, %s, %s)"
# d.execute_a_query("insert into student123(rollnum, sname, branch) values (105, 'yaksh', 'commerce')")
m.execute_multiple_queries(query, data_to_insert )
# d.fetch_all_records("select * from student123")
# d.fetch_only_one_record("")

'''
# query = "create database pshah"
# query = "create table st1(rollnum int not null primary key, sname varchar(10) not null, branch varchar(10) not null)"
# query = "insert into st1(rollnum, sname, branch) values (%s, %s, %s)"
# value= [(103,"jaymin", "ITtech"), (102,"neha", "mba"), (104,"jacob", "test eng")]
# query = "alter table st1 add section varchar(10) default 'A'"
#select 1st five or select 5 starting from 3rd position--->select * from student LIMIT 5 or
select * from student LIMIT 5 OFFSET 2(to not select 1st 2 rows
'''
# m =mysql_connect()
# m.connect()
# m.fetch_all_records("Select * from student123")
# m.fetch_only_one_record("select sname from student123 where rollnum = 103")
# data_to_insert = "[(106, 'vedant', 'grade8'),(107, 'apurv', 'grade9'),(108, 'vanshi', 'grade10')]"
# query = "insert into student123(rollnum, sname, branch) values (%s, %s, %s)"
# d.execute_a_query("insert into student123(rollnum, sname, branch) values (105, 'yaksh', 'commerce')")
# m.execute_multiple_queries(query, data_to_insert)
# m.execute_a_query("insert into student123(rollnum, sname, branch) values (108, 'vanshi', 'grade10')")