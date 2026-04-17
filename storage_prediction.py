from database import connect

def save_prediction(label):
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO predictions (label) VALUES (?)",
        (label,)
    )
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    save_prediction(1)