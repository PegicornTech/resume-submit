import mysql.connector

# Define your MySQL database credentials
host = "localhost"
username = "jobs"
password = "jobapplication"
database = "applicants"

try:
    # Create a MySQL connection
    connection = mysql.connector.connect(
        host=host,
        user=username,
        password=password
    )

    # Create a cursor to execute SQL statements
    cursor = connection.cursor()

    # Create the database (if it doesn't already exist)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

    # Use the database
    cursor.execute(f"USE {database}")

    # Create the "applicants" table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applicants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            email VARCHAR(255) NOT NULL,
            address TEXT NOT NULL,
            former_employer VARCHAR(255) NOT NULL,
            position VARCHAR(255) NOT NULL,
            submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    print("Database and table created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

