import sqlite3

DB_NAME = "predictions.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()