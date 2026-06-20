import sqlite3

DB_PATH = "database/users.db"

def register_user(username, email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(username,email,password)
            VALUES(?,?,?)
            """,
            (username, email, password)
        )

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user
def save_profile(
    user_id,
    name,
    degree,
    branch,
    year,
    cgpa,
    skills,
    interests
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO profiles(
            user_id,
            name,
            degree,
            branch,
            year,
            cgpa,
            skills,
            interests
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            user_id,
            name,
            degree,
            branch,
            year,
            cgpa,
            skills,
            interests
        )
    )

    conn.commit()
    conn.close()