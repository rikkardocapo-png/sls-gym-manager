import mysql.connector
from mysql.connector import Error

# Database connection details
host = "sql307.infinityfree.com"
user = "if0_37349723"
port = 3306
password = "REDACTED"
database = "if0_37349723_GymDatabase"

def check_mysql_connection():
    try:
        # Connect without specifying the port
        connection = mysql.connector.connect(
            host=host,
            user=user,
            port=int(port),
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Successfully connected to the MySQL server.")
            connection.close()
        else:
            print("Connection to MySQL server failed.")

    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_mysql_connection()
