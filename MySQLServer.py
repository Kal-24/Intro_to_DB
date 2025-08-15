import mysql.connector
from mysql.connector import errorcode

# Replace these values with your own MySQL server credentials
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password_here'  # Replace with your actual password
DB_NAME = 'alx_book_store'

try:
    # Connect to MySQL server (not to a specific database yet)
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Create database (if it doesn't exist)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Clean up: close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
