from db_config import get_connection
conn = get_connection()
cur = conn.cursor()
query = """
SELECT users.name, orders.order_id, orders.amount
FROM users
INNER JOIN orders ON users.user_id = orders.user_id"""

cur.execute(query)

joined_results = cur.fetchall()
for name, order_id, amount in joined_results:
    print(f"User: {name} | Order ID: {order_id} | Amount: ${amount:.2f}")
cur.close()
conn.close()