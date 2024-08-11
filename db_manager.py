import mysql.connector

# Database connection configuration
db_config = {
    'user': 'root',
    'password': 'taekook9597',
    'host': 'localhost',
    'database': 'calculator'
}

def connect_db():
    return mysql.connector.connect(**db_config)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        expression TEXT NOT NULL,
        result TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_calculation(expression, result):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (expression, result) VALUES (%s, %s)", (expression, result))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_history():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT expression, result, timestamp FROM history ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

create_table()
