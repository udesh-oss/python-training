from db_config import get_connection

conn = get_connection()
cur = conn.cursor()
cur.execute("INSERT INTO users (user_id, name) VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")
cur.execute("INSERT INTO orders (order_id, amount, user_id) VALUES (101, 50.00, 1), (102, 20.00, 2), (103, 15.00, 1)")
conn.commit()
cur.close()
conn.close()