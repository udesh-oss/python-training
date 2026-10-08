from db_config import get_connection
conn = get_connection()
cur = conn.cursor()
cur.execute(""" SELECT user_id, COUNT(order_id) AS total_orders
            FROM orders
            GROUP BY user_id
            ORDER BY user_id ASC;""")

order_counts = cur.fetchall()
for user_id, total_orders in order_counts:
    print(f"User ID {user_id} made {total_orders} order(s).")
cur.close()
conn.close()