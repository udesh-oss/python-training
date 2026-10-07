import psycopg2

conn = psycopg2.connect(
        dbname="PythonPractice",
        user="postgres",
        password="@31March1998",
        host="localhost",
        port="5432"
    )
#Open a cursor to perform database operations
cur = conn.cursor()
#execute a command: this creates a new table
cur.execute("""CREATE TABLE datacamp_courses(
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR (50) UNIQUE NOT NULL,
            course_instructor VARCHAR (100) NOT NULL,
            topic VARCHAR (20) NOT NULL);
            """)
#make the changes to the database persistent
conn.commit()
#close cursor and communication with database
cur.close()
conn.close()

