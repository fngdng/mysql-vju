
import sqlite3

conn = sqlite3.connect("./DB/japanese.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS WordHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT NOT NULL,
    word_id INTEGER NOT NULL,
    topic TEXT NOT NULL,
    viewed_at TEXT NOT NULL,
    is_last_viewed INTEGER DEFAULT 0,
    FOREIGN KEY (user_email) REFERENCES Users(email),
    FOREIGN KEY (word_id) REFERENCES Words(id)
);
""")

conn.commit()
conn.close()
print("✅ Đã tạo bảng WordHistory (theo chủ đề) thành công.")
