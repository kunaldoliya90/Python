import mysql.connector

def connect_to_mysql(host, user, password, database):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Perform database operations here

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Close the database connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL database connection closed")

# Test the function
host = "localhost"  # Replace with your MySQL host
user = "kunald"  # Replace with your MySQL username
password = "test123"  # Replace with your MySQL password
database = "db"  # Replace with your MySQL database name

connect_to_mysql(host, user, password, database)
