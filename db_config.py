import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="PythonPractice",
        user="postgres",
        password="@31March1998",
        host="localhost",
        port="5432"
    )