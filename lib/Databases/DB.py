import mysql.connector
from mysql.connector import Error
from src import get_config
from Database_connection import get_connection
from datetime import datetime, date


class Db:
    def __init__(self, table_name=None):
        self.table_name = self.validate_table()

    @staticmethod
    def validate_table(self, table_name):
        try:
            db_connection = Database_connection.get_connection()
            exists = Database_connection.table_exists(table_name)

            if exists:
                return table_name
            else:
                return "product"
        except Error as e:
            raise Exception(f"Error : {e}")

        finally:
            if db_connection.is_connected():
                cursor.close()

    '''
    NO Need to pass any argument to get_details()
    '''
    @staticmethod
    def get_details(self):
        try:
            connection = Database_connection.get_connection()
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name}")
            results = cursor.fetchall()
            cursor.close()
            return results

        except Error as e:
            raise Exception(f"Error : {e}")

        finally:
            if connection.is_connected():
                connection.close()
                print(f"Connection is now closed")

    '''
    data -> data must be in dictionary format
    '''
    @staticmethod
    def set_details(self, data):
        result = False
        try:
            connection = Database_connection.get_connection()
            cursor = connection.cursor()
            columns = ', '.join(data.keys())
            values = ', '.join([f"'{value}'" for value in data.values()])

            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values})"
            cursor.execute(query)

            # Commit the changes to make them permanent in the database
            connection.commit()
            cursor.close()
            result = True
            return result

        except Error as e:
            raise Exception(f"Error : {e}")

        finally:
            if connection.is_connected():
                connection.close()

    @staticmethod
    def get_particular_details(self, coloumn_detail, user_product_detail):
        '''
        in this methid is i metioned i particular parameter of the user products and db table coloumn parameter
        '''
        try:
            connection = Database_connection.get_connection()
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {coloumn_detail} = '{user_product_detail}'"
            cursor.execute(query)
            product_details = cursor.fetchone()
            cursor.close()
            return product_details

        except Error as e:
            raise Exception(f"Error : {e}")

        finally:
            if connection.is_connected():
                connection.close()

    '''
    TODO: one user bill --> open a db connections and add the details to the db and close the connections
    
    '''
