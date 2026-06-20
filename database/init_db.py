import sqlite3

conn = sqlite3.connect("database/users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT
)
""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS profiles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    degree TEXT,
    branch TEXT,
    year TEXT,
    cgpa REAL,
    skills TEXT,
    interests TEXT,
    profile_score INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")