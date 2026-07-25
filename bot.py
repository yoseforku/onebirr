import os
import mysql.connector

print("Connecting to MySQL...")

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_disabled=False,
    )

    print("✅ Connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    print("MySQL Version:", cursor.fetchone()[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)
