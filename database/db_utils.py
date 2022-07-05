from abc import ABC,abstractmethod
import mysql.connector
from python_mysql_dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error

class Database_Class(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_a_query(self, connection, query_to_execute):
        pass

    @abstractmethod
    def execute_multiple_queries(self, connection, queries_to_execute, value):
        pass

    # @abstractmethod
    # def fetch_records(self, connection, query):
    #     pass

class Mysql_Connect(Database_Class):
    """ Connect to MySQL database """
    def connect(self):
        # conn = None
        try:
            connection = read_db_config()
            conn = MySQLConnection()
            if conn.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                print("connection is successful************")
                return connection
            else:
                return None
        except Error as e:
            print("Error while connecting to MySQL", e)
            return None

    def execute_a_query(self, connection, query_to_execute):
        cursor = connection.cursor()
        # global connection timeout arguments
        '''global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)'''
        query = query_to_execute
        try:
            cursor.execute(query)
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
            return records
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
            return None
        finally:
            cursor.close()
            return None


    def fetch_only_one_record(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            record = cursor.fetchone()
            print(record)
            for entry in record:
                print(entry)
            return record
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
            return None
        finally:
            cursor.close()
            return None



'''
# query = "create database pshah"
# query = "create table st1(rollnum int not null primary key, sname varchar(10) not null, branch varchar(10) not null)"
# query = "insert into st1(rollnum, sname, branch) values (%s, %s, %s)"
# value= [(103,"jaymin", "ITtech"), (102,"neha", "mba"), (104,"jacob", "test eng")]
# query = "alter table st1 add section varchar(10) default 'A'"
'''

