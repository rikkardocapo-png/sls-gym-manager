import pymysql


def test_connection():
    # Database credentials
    host = "sql.slsprojects.it"
    user = "slsproje37171"
    password = "REDACTED"
    database = "slsproje37171"
    port = 3306  # Default MySQL port

    try:
        print("Attempting to connect to the database...")
        # Establish a connection
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            connect_timeout=10  # Timeout in seconds
        )
        print("Connection successful!")

        # Get and print server information
        server_info = connection.get_server_info()
        print(f"Connected to MySQL Server version: {server_info}")

    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the connection if it was established
        if 'connection' in locals() and connection.open:
            connection.close()
            print("Connection closed.")


# Run the connection test
test_connection()
