import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='128.0.10.5',  # Change if your MySQL server is hosted elsewhere
            user='shad',  # Replace with your MySQL username
            password='root',
            database='my_test_db',
            auth_plugin='mysql_native_password'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()