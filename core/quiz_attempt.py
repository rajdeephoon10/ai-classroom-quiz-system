import json
from database.db import cursor

def get_quiz(quiz_code):

    cursor.execute("SELECT quiz_json FROM quizzes WHERE quiz_code=?",(quiz_code,))
    result = cursor.fetchone()

    if result:
        return json.loads(result[0])

    return None