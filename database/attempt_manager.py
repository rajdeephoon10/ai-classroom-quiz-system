from database.db import get_connection


def store_attempt(session_code, student_name, score, total):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attempts (session_code, student_name, score, total) VALUES (?, ?, ?, ?)",
        (session_code, student_name, score, total)
    )

    conn.commit()
    conn.close()


def get_session_attempts(session_code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_name, score, total FROM attempts WHERE session_code=?",
        (session_code,)
    )

    results = cursor.fetchall()
    conn.close()

    return results