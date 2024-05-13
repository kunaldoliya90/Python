# Write a python program to perform following database operations:
# i) create ii) alter iii) insert iv) update v) drop vi) delete

import mysql.connector

# Connect to the MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="db"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

        return connection

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

# Create a table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                department VARCHAR(255)
            )
        """)
        print("Table 'employees' created successfully")

    except mysql.connector.Error as e:
        print("Error creating table:", e)

# Alter table
def alter_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            ALTER TABLE employees
            ADD COLUMN salary INT
        """)
        print("Table 'employees' altered successfully")

    except mysql.connector.Error as e:
        print("Error altering table:", e)

# Insert data into the table
def insert_data(connection):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
        values = ("John", 30, "HR")
        cursor.execute(sql, values)
        connection.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as e:
        print("Error inserting data:", e)

# Update data in the table
def update_data(connection):
    try:
        cursor = connection.cursor()
        sql = "UPDATE employees SET department = %s WHERE name = %s"
        values = ("Finance", "John")
        cursor.execute(sql, values)
        connection.commit()
        print("Data updated successfully")

    except mysql.connector.Error as e:
        print("Error updating data:", e)

# Drop table
def drop_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS employees")
        print("Table 'employees' dropped successfully")

    except mysql.connector.Error as e:
        print("Error dropping table:", e)

# Delete data from the table
def delete_data(connection):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM employees WHERE name = %s"
        values = ("John",)
        cursor.execute(sql, values)
        connection.commit()
        print("Data deleted successfully")

    except mysql.connector.Error as e:
        print("Error deleting data:", e)

# Main function
def main():
    connection = connect_to_mysql()

    # Create table
    create_table(connection)

    # Insert data
    insert_data(connection)

    # Alter table
    alter_table(connection)

    # Update data
    update_data(connection)

    # Delete data
    delete_data(connection)

    # Drop table
    drop_table(connection)

    # Close the connection
    if connection.is_connected():
        connection.close()
        print("MySQL database connection closed")

if __name__ == "__main__":
    main()
