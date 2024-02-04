import mysql.connector
from mysql.connector import Error
from src import get_config
from Database_connection import get_connection
from datetime import datetime, date


class Billing:
    def __init__(self,db=None):
        self.db = db if db else "billing"
        
        
    @staticmethod
    def get_products_details(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        '''
        TODO: implement in Db()
        '''
        # try:
        #     connection = Database_connection.get_connection()
        #     cursor = conn.cursor()
        #     cursor.execute(f"SELECT * FROM {self.db}")
        #     results = cursor.fetchall()
        #     cursor.close()
        #     print(results)
        #     return results
        
        # except Exception as e:
        #     raise Exception(f"Error: {e}")
            
        # finally:
        #     if connection.is_connected():
        #         connection.close()
        #         print(f"Connection now closed --> {current_time}")
           
            
    @staticmethod
    def set_products_details(self,product_id,date,quantity,price,total_bills,total_products):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            connection = Database_connection.get_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {self.db} (product_id,date,quantity,price,total_bills,total_products) VALUES ('{product_id}','{date}','{quantity}','{price}','{total_bills}','{total_products}')"
            
        except Error as e:
            raise Exception(f"Error: {e}")
        
        finally:
            Database_connection.close_connection()
            
    
