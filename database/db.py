import sqlite3

DB_NAME = "quiz_system.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_code TEXT PRIMARY KEY,
        topic TEXT,
        quiz_data TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_code TEXT,
        student_name TEXT,
        score INTEGER,
        total INTEGER
    )
    """)

    conn.commit()
    conn.close()