import mysql.connector
from mysql.connector import Error
from src import get_config

class Database_connection:
    _conn = None

    @staticmethod
    def get_connection():
        if Database_connection._conn is None:
            try:
                servername = get_config("client_mysql_db_servername")
                username = get_config("client_mysql_db_username")
                password = get_config("client_mysql_db_password")
                dbname = get_config("client_mysql_db_dbname")

                conn = mysql.connector.connect(
                    host=servername,
                    user=username,
                    password=password,
                    database=dbname
                )

                if conn.is_connected():
                    print("Connected to MySQL Server")

                    Database_connection._conn = conn  

                    return Database_connection._conn
                else:
                    raise Exception("Connection failed")

            except Error as e:
                print(f"Error: {e}")
                raise Exception("Connection failed")

        else:
            return Database_connection._conn


# try:
#     db_connection = Database_connection.get_connection()  
# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     if 'db_connection' in locals() and db_connection.is_connected():
#         db_connection.close()
#         print("Connection closed")
