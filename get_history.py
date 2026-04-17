from database import connect

def fetch_history():
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")
    
    rows = cursor.fetchall()
    
    conn.close()
    
    return rows


if __name__ == "__main__":
    
    history = fetch_history()
    
    for row in history:
        print(row)