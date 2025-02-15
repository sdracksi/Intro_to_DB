import mysql.connector
import sys

# Get database name from command line argument
db_name = sys.argv[1] if len(sys.argv) > 1 else 'alx_book_store'

try:
    # Establish connection to MySQL server
    conn = mysql.connector.connect(
        host='128.0.10.5',  # Change if necessary
        user='shad',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='alx_book_store'
    )
    
    cursor = conn.cursor()
    
    # Query to list all tables
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    
    # Print table names
    for table in tables:
        print(table[0])
    
    # Close connection
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
