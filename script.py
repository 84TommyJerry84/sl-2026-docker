print("Bonjour depuis mon conteneur Docker !")

import psycopg2


connection = psycopg2.connect(
    host="db",
    database="dockerdb",
    user="admin",
    password="admin",
    port=5432
)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS batch_test (
        id SERIAL PRIMARY KEY,
        message VARCHAR(255)
    )
""")

cursor.execute("""
    INSERT INTO batch_test (message)
    VALUES (%s)
""", ("Bonjour depuis le batch Python",))

connection.commit()

cursor.execute("SELECT * FROM batch_test")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()