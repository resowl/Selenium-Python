from abc import ABC,abstractmethod
import mysql.connector
from mysql.connector import Error

class Database_Class(ABC):
    @abstractmethod
    def connect_to_database(self, host, user, password, database, port):
        pass

    @abstractmethod
    def execute_a_query(self, connection, query_to_execute):
        pass

    @abstractmethod
    def execute_multiple_queries(self, connection, queries_to_execute, value):
        pass

    @abstractmethod
    def fetch_records(self, connection, query):
        pass

class mysql_connect(Database_Class):
    def connect_to_database(self, host, user, password, database, port):
        try:
            # connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database="prjay", port= "port1")
            connection = mysql.connector.connect(host=host, user=user, passwd=password, database=database, port=port)
            if connection.is_connected():
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



