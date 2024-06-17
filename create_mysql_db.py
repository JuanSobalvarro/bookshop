import mysql.connector
from mysql.connector import Error


def create_database(host, user, password, database_name, port):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database query
            create_db_query = f"CREATE DATABASE {database_name}"

            # Execute the create database query
            cursor.execute(create_db_query)
            print(f"Database '{database_name}' created successfully.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":

    host = 'localhost'
    user = 'root'
    password = 'root'
    database_name = 'bookshop'
    port = 4444

    create_database(host, user, password, database_name, port)
