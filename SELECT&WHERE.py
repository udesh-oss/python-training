from db_config import get_connection
conn = get_connection()
cur = conn.cursor()
min_amount = 30.00
cur.execute("SELECT * FROM orders WHERE amount > %s;", (min_amount,))
orders = cur.fetchall()
for order in orders:
    print(order)
cur.close()
conn.close()