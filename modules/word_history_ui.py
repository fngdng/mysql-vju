import sqlite3
import tkinter as tk
from tkinter import ttk
from modules.menu import show_menu
from modules.db_helper import get_db_path

def show_word_history(user_name):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    # Lấy email người dùng
    cursor.execute("SELECT email FROM Users WHERE name = ?", (user_name,))
    user = cursor.fetchone()
    if not user:
        return
    user_email = user[0]

    # Lấy dữ liệu lịch sử học từ
    cursor.execute("""
        SELECT Words.japanese, Words.romaji, Words.meaning, WordHistory.topic, WordHistory.viewed_at
        FROM WordHistory
        JOIN Words ON WordHistory.word_id = Words.id
        WHERE WordHistory.user_email = ?
        ORDER BY WordHistory.viewed_at DESC
    """, (user_email,))
    rows = cursor.fetchall()
    conn.close()

    # Giao diện
    win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win,1100, 500)
    win.title("Lịch sử học từ")
    win.geometry("1100x500")
    win.configure(bg="#f7f9fa")

    tk.Label(win, text="📚 Lịch sử học từ", font=("Arial", 18, "bold"), bg="#f7f9fa").pack(pady=20)

    frame = tk.Frame(win, bg="#f7f9fa")
    frame.pack(fill="both", expand=True, padx=20)

    tree = ttk.Treeview(frame, columns=("japanese", "romaji", "meaning", "topic", "time"), show="headings")
    tree.heading("japanese", text="Từ Nhật")
    tree.heading("romaji", text="Romaji")
    tree.heading("meaning", text="Nghĩa")
    tree.heading("topic", text="Chủ đề")
    tree.heading("time", text="Thời gian học")
    tree.pack(fill="both", expand=True)

    for row in rows:
        tree.insert("", "end", values=row)

    tk.Button(win, text="⬅ Quay lại menu", font=("Arial", 11), bg="#dfe6e9",
              command=lambda: (win.destroy(), show_menu(user_name))).pack(pady=10)

    win.mainloop()
