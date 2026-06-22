import sqlite3

DB_PATH = "database/users.db"


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
        SELECT * FROM profiles
        WHERE user_id=?
        """,
        (user_id,)
    )

    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE profiles
            SET
                name=?,
                degree=?,
                branch=?,
                year=?,
                cgpa=?,
                skills=?,
                interests=?
            WHERE user_id=?
            """,
            (
                name,
                degree,
                branch,
                year,
                cgpa,
                skills,
                interests,
                user_id
            )
        )

    else:

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


def get_profile(user_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM profiles
        WHERE user_id=?
        """,
        (user_id,)
    )

    profile = cursor.fetchone()

    conn.close()

    return profile