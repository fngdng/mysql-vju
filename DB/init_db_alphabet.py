
import sqlite3

# Kết nối đến CSDL
conn = sqlite3.connect("./DB/japanese.db")
cursor = conn.cursor()

# Tạo bảng Alphabets
cursor.execute("""
CREATE TABLE IF NOT EXISTS Alphabets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hiragana TEXT NOT NULL,
    katakana TEXT NOT NULL,
    romaji TEXT NOT NULL
);
""")

# Dữ liệu bảng chữ cái cơ bản (hàng a, i, u, e, o)
alphabet_data = [
    ("あ", "ア", "a"),
    ("い", "イ", "i"),
    ("う", "ウ", "u"),
    ("え", "エ", "e"),
    ("お", "オ", "o"),
    ("か", "カ", "ka"),
    ("き", "キ", "ki"),
    ("く", "ク", "ku"),
    ("け", "ケ", "ke"),
    ("こ", "コ", "ko"),
    ("さ", "サ", "sa"),
    ("し", "シ", "shi"),
    ("す", "ス", "su"),
    ("せ", "セ", "se"),
    ("そ", "ソ", "so"),
    ("た", "タ", "ta"),
    ("ち", "チ", "chi"),
    ("つ", "ツ", "tsu"),
    ("て", "テ", "te"),
    ("と", "ト", "to"),
    ("な", "ナ", "na"),
    ("に", "ニ", "ni"),
    ("ぬ", "ヌ", "nu"),
    ("ね", "ネ", "ne"),
    ("の", "ノ", "no")
]

# Chèn dữ liệu nếu bảng trống
cursor.execute("SELECT COUNT(*) FROM Alphabets")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO Alphabets (hiragana, katakana, romaji) VALUES (?, ?, ?)", alphabet_data)

conn.commit()
conn.close()
print("✅ Đã tạo bảng Alphabets và chèn dữ liệu.")
