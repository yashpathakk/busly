import mysql.connector
from mysql.connector import Error


def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pathak0101",
            database="busly"
        )

        if connection.is_connected():
            print("Connected to Busly database successfully!")
            return connection

    except Error as e:
        print("Database Connection Error:", e)
        return None

def close_database(connection):
    if connection is not None and connection.is_connected():
        connection.close()
        print("Database connection closed.")
