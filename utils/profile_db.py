import sqlite3

DB_PATH = "database/users.db"

def get_profile(user_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM profiles WHERE user_id=?",
        (user_id,)
    )

    profile = cursor.fetchone()

    conn.close()

    return profile