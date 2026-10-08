from db_config import get_connection

conn = get_connection()
cur = conn.cursor()
#Create a parent table
cur.execute("""CREATE TABLE users(
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL);
            """)
#Create the child table
cur.execute("""CREATE TABLE orders(
            order_id INTEGER PRIMARY KEY,
            amount DECIMAL(10,2),
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id));
            """)

conn.commit()
cur.close()
conn.close()
