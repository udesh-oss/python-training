from db_config import get_connection

conn = get_connection()
cur = conn.cursor()

try:
    cur.execute(
        "INSERT INTO users (user_id, name) VALUES (%s, %s);", (4, "David")
    )

    cur.execute(
        "INSERT INTO orders (order_id, user_id, amount) VALUES (%s, %s, %s);", (104, 4, 15.00),
    )

    conn.commit()
    print("Transaction successfully committed! Both enteries saved.")
except Exception as error:
    conn.rollback()
    print(f"Transaction failed and was rolled back Error: {error}")
finally:
    cur.close()
    conn.close()