import sqlite3

DB_NAME = "sentiment.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT,
            sentimen TEXT,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def insert_history(review, sentimen, confidence):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO history (review, sentimen, confidence) VALUES (?, ?, ?)",
              (review, sentimen, confidence))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, review, sentimen, confidence, timestamp FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows
