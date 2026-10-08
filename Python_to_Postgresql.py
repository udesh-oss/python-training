from db_config import get_connection
try:
    conn = get_connection()
    cur = conn.cursor()    
    # Run a basic query to verify connectivity
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    
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
