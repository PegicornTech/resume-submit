import mysql.connector

# Define your MySQL root user credentials
host = "localhost"
root_username = "root"
root_password = "root_password"  # Replace with your root password
database = "applicants"
user_to_grant = "jobs"
user_password = "jobapplication"  # Set the desired password for the "jobs" user

try:
    # Create a MySQL connection with root credentials
    connection = mysql.connector.connect(
        host=host,
        user=root_username,
        password=root_password
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

    # Create a new MySQL user "jobs" and grant full privileges on the "applicants" database
    cursor.execute(f"CREATE USER '{user_to_grant}'@'localhost' IDENTIFIED BY '{user_password}'")
    cursor.execute(f"GRANT ALL PRIVILEGES ON {database}.* TO '{user_to_grant}'@'localhost'")
    cursor.execute("FLUSH PRIVILEGES")

    print("Database and table created successfully.")
    print(f"User '{user_to_grant}' granted full privileges on database '{database}'.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

