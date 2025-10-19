import mysql.connector
from mysql.connector import Error

def list_tables(database_name):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # 🔸 Replace with your MySQL root password
            database=database_name
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            if tables:
                print(f"Tables in database '{database_name}':")
                for table in tables:
                    print(table[0])
            else:
                print(f"No tables found in database '{database_name}'")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 task_3.py <database_name>")
    else:
        db_name = sys.argv[1]
        list_tables(db_name)

