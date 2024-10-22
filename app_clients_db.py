import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='172.18.1.13',       # Change if the database is hosted elsewhere
            user='app01',   # Your MySQL username
            password='Sucesso_2025', # Your MySQL password
            database='db_users'     # The name of your database
        )

        if connection.is_connected():
            print("Successfully connected to the database")

            # Optional: Get some server info
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")

            # Optional: Execute a query to fetch the databases
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to the database: {record}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_db()
