import tkinter as tk
import sqlite3
from tkinter import messagebox
from modules.menu import show_menu

def show_progress(user_name):
    conn = sqlite3.connect("./DB/japanese.db")
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM Users WHERE name = ?", (user_name,))
    user = cursor.fetchone()
    if not user:
        messagebox.showerror("Lỗi", "Không tìm thấy người dùng.")
        return

    user_email = user[0]

    cursor.execute("""
        SELECT COUNT(DISTINCT word_id), SUM(correct), SUM(incorrect)
        FROM Progress
        WHERE user_email = ?
    """, (user_email,))
    result = cursor.fetchone()
    conn.close()

    total_words = result[0] or 0
    total_correct = result[1] or 0
    total_incorrect = result[2] or 0

    win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win, 500, 300)
    win.title("Tiến độ học tập")
    win.geometry("500x300")
    win.configure(bg="#fef9e7")

    tk.Label(win, text=f"📈 Tiến độ học của: {user_name}", font=("Arial", 16, "bold"), bg="#fef9e7").pack(pady=20)
    tk.Label(win, text=f"🔸 Tổng số câu đã làm: {total_words}", font=("Arial", 13), bg="#fef9e7").pack(pady=5)
    tk.Label(win, text=f"✅ Trả lời đúng: {total_correct}", font=("Arial", 13), bg="#fef9e7").pack(pady=5)
    tk.Label(win, text=f"❌ Trả lời sai: {total_incorrect}", font=("Arial", 13), bg="#fef9e7").pack(pady=5)

    tk.Button(win, text="⬅ Quay lại menu", font=("Arial", 11), bg="#dfe6e9",
              command=lambda: (win.destroy(), show_menu(user_name))).pack(pady=30)

    win.mainloop()
