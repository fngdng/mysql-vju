# modules/topic_words.py
def show_words_by_topic(user_name, topic):
    import tkinter as tk
    import sqlite3
    from modules.choose_topic import show_topic_selection
    from modules.db_helper import get_db_path

    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT japanese, romaji, meaning FROM Words WHERE topic = ?", (topic,))
    words = cursor.fetchall()
    last_word_id = lay_tu_dung_lai(user_name, topic)

    # Tìm vị trí trong danh sách
    start_index = 0
    if last_word_id:
        cursor.execute("SELECT japanese, romaji, meaning FROM Words WHERE id = ?", (last_word_id,))
        last_word = cursor.fetchone()
        if last_word and last_word in words:
            start_index = words.index(last_word)
    conn.close()

    index = [start_index]

    def update_display():
        if 0 <= index[0] < len(words):
            jp, romaji, vi = words[index[0]]
            word_label.config(text=f"Từ: {jp}\nRomaji: {romaji}\nNghĩa: {vi}")
            status_label.config(text=f"{index[0]+1}/{len(words)}")
            ghi_lich_su_theo_chu_de(user_name, jp, romaji, vi, topic)

    def next_word():
        if index[0] < len(words) - 1:
            index[0] += 1
            update_display()

    def prev_word():
        if index[0] > 0:
            index[0] -= 1
            update_display()

    win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win, 600, 400)
    win.title(f"Từ vựng - Chủ đề: {topic}")
    win.geometry("600x400")
    win.configure(bg="#f1f2f6")

    tk.Label(win, text=f"📖 Chủ đề: {topic}", font=("Arial", 16, "bold"), bg="#f1f2f6").pack(pady=10)

    word_label = tk.Label(win, text="", font=("Arial", 14), bg="#f1f2f6", justify="center")
    word_label.pack(pady=20)

    status_label = tk.Label(win, text="", font=("Arial", 12), bg="#f1f2f6")
    status_label.pack()

    nav_frame = tk.Frame(win, bg="#f1f2f6")
    tk.Button(nav_frame, text="⬅ Trước", font=("Arial", 11), command=prev_word).pack(side="left", padx=10)
    tk.Button(nav_frame, text="Tiếp ➡", font=("Arial", 11), command=next_word).pack(side="left", padx=10)
    nav_frame.pack(pady=10)

    tk.Button(win, text="⬅ Quay lại chọn chủ đề", font=("Arial", 11), bg="#dfe6e9", command=lambda: (win.destroy(), show_topic_selection(user_name))).pack(pady=10)

    if words:
        update_display()
    else:
        word_label.config(text="❌ Không có từ vựng nào trong chủ đề này.")
        status_label.config(text="0/0")

    win.mainloop()

from datetime import datetime
import sqlite3
from modules.db_helper import get_db_path

def ghi_lich_su_theo_chu_de(user_name, japanese, romaji, meaning, topic):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    # Lấy email người dùng
    cursor.execute("SELECT email FROM Users WHERE name = ?", (user_name,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return
    user_email = user[0]

    # Lấy word_id
    cursor.execute("SELECT id FROM Words WHERE japanese = ? AND romaji = ? AND meaning = ?", 
                   (japanese, romaji, meaning))
    word = cursor.fetchone()
    if not word:
        conn.close()
        return
    word_id = word[0]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Reset tất cả is_last_viewed về 0 theo user + topic
    cursor.execute("UPDATE WordHistory SET is_last_viewed = 0 WHERE user_email = ? AND topic = ?", 
                   (user_email, topic))

    # Ghi dòng mới
    cursor.execute("""
        INSERT INTO WordHistory (user_email, word_id, viewed_at, topic, is_last_viewed)
        VALUES (?, ?, ?, ?, 1)
    """, (user_email, word_id, now, topic))

    conn.commit()
    conn.close()
    
def lay_tu_dung_lai(user_name, topic):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM Users WHERE name = ?", (user_name,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return None
    user_email = user[0]

    cursor.execute("""
        SELECT word_id FROM WordHistory
        WHERE user_email = ? AND topic = ? AND is_last_viewed = 1
    """, (user_email, topic))

    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

