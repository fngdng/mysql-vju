import sqlite3

def init_progress_table():
    conn = sqlite3.connect("./DB/japanese.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        word_id INTEGER,
        correct INTEGER DEFAULT 0,
        incorrect INTEGER DEFAULT 0,
        last_practiced TEXT,
        FOREIGN KEY (word_id) REFERENCES Words(id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Đã tạo bảng Progress nếu chưa có.")

if __name__ == "__main__":
    init_progress_table()
