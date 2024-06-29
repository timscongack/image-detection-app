import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('detections.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            object TEXT,
            timestamp TEXT,
            image_file_path TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized")

def save_detection(object_name, image_file_path):
    try:
        conn = sqlite3.connect('detections.db')
        c = conn.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO detections (object, timestamp, image_file_path) VALUES (?, ?, ?)",
                  (object_name, timestamp, image_file_path))
        conn.commit()
        conn.close()
        print(f"Detection saved: {object_name}, {image_file_path}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")