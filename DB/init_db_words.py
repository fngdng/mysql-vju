import sqlite3

# Kết nối SQLite (tạo nếu chưa tồn tại)
conn = sqlite3.connect("japanese.db")
cursor = conn.cursor()

# Tạo bảng Words
cursor.execute("""
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    japanese TEXT NOT NULL,
    kana TEXT,
    meaning TEXT,
    topic TEXT
)
""")

conn.commit()
conn.close()

print(" Đã tạo xong cơ sở dữ liệu và bảng Words.")
