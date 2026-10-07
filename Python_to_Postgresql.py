import psycopg2

try:
    # Attempt to establish the connection
    connection = psycopg2.connect(
        dbname="PythonPractice",
        user="postgres",
        password="@31March1998",
        host="localhost",
        port="5432"
    )
    
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()
    
    # Run a basic query to verify connectivity
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print("Connection successful!")
    print("PostgreSQL Database Version:", db_version[0])

except Exception as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Clean up and close connection resources
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
        print("Database connection closed.")
