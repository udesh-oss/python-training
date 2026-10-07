import psycopg2

conn = psycopg2.connect(
        dbname="PythonPractice",
        user="postgres",
        password="@31March1998",
        host="localhost",
        port="5432"
    )

cur = conn.cursor()

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to SQL','Izzy Weber','Julia')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Analyzing Survey Data in Python','EbunOluwa Andrew','Python')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to ChatGPT','James Chapman','Theory')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to Statistics in R','Maggie Matsui','R')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Hypothesis Testing in Python','James Chapman','Python')");

conn.commit()
cur.close()
conn.close()