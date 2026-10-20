
import mysql.connector
from mysql.connector import Error


# Connect to Busly Database

def connect_database():

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pathak0101",
            database="busly"
        )

        if conn.is_connected():
            return conn

    except Error as error:
        print("Database connection error:", error)

    return None
