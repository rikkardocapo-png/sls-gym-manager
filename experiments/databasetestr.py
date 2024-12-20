import mysql.connector
from mysql.connector import Error

def test_database_connection():
    host = "m-06.th.seeweb.it"
    user = "slsproje37171"
    database = "slsproje37171"
    port = 3306
    password = "REDACTED"

    try:
        print("Attempting to connect to the database...")
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )

        if connection.is_connected():
            print("Connection successful!")
            server_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {server_info}")
            return True

    except Error as e:
        print(f"Error: Unable to connect to the database.\n{e}")
        return False

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed.")

# Run the test
test_database_connection()
