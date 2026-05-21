import json
from database.db import cursor,conn

def save_quiz(title,quiz,quiz_code):

    cursor.execute(
    "INSERT INTO quizzes(title,quiz_json,quiz_code) VALUES(?,?,?)",
    (title,json.dumps(quiz),quiz_code)
    )

    conn.commit()