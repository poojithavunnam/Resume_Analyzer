import sqlite3

DB_NAME = "database.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS analyses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        filename TEXT,
        role TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()