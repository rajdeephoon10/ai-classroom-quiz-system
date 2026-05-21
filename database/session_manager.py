import random
import string
import json
from database.db import get_connection

def generate_session_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_session(topic, quiz):
    session_code = generate_session_code()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sessions (session_code, topic, quiz_data) VALUES (?, ?, ?)",
        (session_code, topic, json.dumps(quiz))
    )

    conn.commit()
    conn.close()

    return session_code

def get_session_quiz(session_code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT quiz_data FROM sessions WHERE session_code=?",
        (session_code,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return json.loads(result[0])
    return None