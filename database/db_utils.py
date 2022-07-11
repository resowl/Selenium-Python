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
    def fetch_all_records(self, query):
        pass

    @abstractmethod
    def fetch_only_one_record(self, query):
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
        try:
            cursor.execute(query_to_execute)
            connection.commit()
            print("Query executed successfully********")
            print(cursor.rowcount, "rows printed")
        except:
            connection.rollback()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def execute_multiple_queries(self, queries_to_execute, value):
        connection = self.connect()
        cursor = connection.cursor()
        try:
            result_iterator = cursor.execute(queries_to_execute, value) #value is list of tuples
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query
                print(f"Affected {res.rowcount} rows")
                print("Queries executed successfully********")
            connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
        print(cursor.rowcount, "rows printed")


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
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        try:
            fetch_result = cursor.fetchone()
            print("Json Format:-->", json.dumps(fetch_result, indent=4))
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()

