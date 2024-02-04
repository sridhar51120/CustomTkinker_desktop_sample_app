import mysql.connector
from mysql.connector import Error
from src import get_config
from Database_connection import get_connection
from datetime import datetime, date

class Sales:
    def __init__(self,db=None):
        self.db = db if db else "sales"
    
    