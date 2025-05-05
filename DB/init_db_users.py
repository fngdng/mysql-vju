import sqlite3

conn = sqlite3.connect("./DB/japanese.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    birthday TEXT
);
""")

conn.commit()
conn.close()
print("Xong")
