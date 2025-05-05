
import sqlite3


conn = sqlite3.connect("./DB/japanese.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    japanese TEXT NOT NULL,
    romaji TEXT,
    meaning TEXT,
    topic TEXT
);
""")

conn.commit()
conn.close()
print("✅ Đã tạo bảng Words với cột romaji.")