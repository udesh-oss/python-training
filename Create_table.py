from db_config import get_connection
conn = get_connection()
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

