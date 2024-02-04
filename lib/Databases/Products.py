'''
    Product ID
    Product Name
    Category
    Brand
    Description
    Unit of Measurement (e.g., kg, liter, unit)
    
'''
import mysql.connector
from mysql.connector import Error
from src import get_config
from Database_connection import get_connection
from datetime import datetime

class Products:
    def __init__(self,db=None):
        self.db = db if db else "products"
    
    def create_databse(self):
        pass
    
    @staticmethod
    def get_products_details(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            connection = Database_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.db}")
            results = cursor.fetchall()
            cursor.close()
            print(results)
            return results
        
        except Exception as e:
            raise Exception(f"Error: {e}")
            
        finally:
            if connection.is_connected():
                connection.close()
                print(f"Connection now closed --> {current_time}")
           
            
    @staticmethod
    def set_products_details(self,product_id,product_name,category,brand,description,units_of_measurement,proice):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            connection = Database_connection.get_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {self.db} (product_id,product_name,category,brand, description,units_of_measurement,price) VALUES ('{product_id}','{product_name}','{category}','{brand}','{description}','{units_of_measurement}','{price}')"
            
        except Error as e:
            raise Exception(f"Error: {e}")
        
        finally:
            if connection.is_connected():
                connection.close()
                print(f"Connction is now closed {current_time}")
                
    @staticmethod
    def get_product_detail(self,product_id,fetch_column=None):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            connection = Database_connection.get_connection()
            cursor = conn.cursor()

            cursor.execute(f"SELECT {product_id} FROM {self.db}")
            
            # column_values = Database_connection.execute_query(query, fetch_column=True)
            # print(column_values)
    
            if fetch_column is not None:
                results = [row[0] for row in cursor.fetchall()]
            else:
                results = cursor.fetchall()

            cursor.close()
            return results
        
        except Error as e:
            raise(f"Error Getting a particular product details {e}")
        
        finally:
            if connection.is_connected():
                connection.close()
                print(f"Connection is now closed --> {current_time}")