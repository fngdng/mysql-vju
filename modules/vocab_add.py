def show_vocab_add(user_name):
    import tkinter as tk
    import sqlite3
    from tkinter import messagebox
    from modules.vocab_lookup import show_vocab_lookup
    from modules.db_helper import get_db_path

    add_win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(add_win,600, 500)
    add_win.title("Thêm từ mới")
    add_win.geometry("600x500")
    add_win.configure(bg="#fefae0")

    tk.Label(add_win, text="➕ Thêm từ vựng mới", font=("Arial", 18, "bold"), bg="#fefae0").pack(pady=20)

    fields = ["Từ tiếng Nhật", "Romaji", "Nghĩa tiếng Việt", "Chủ đề"]
    entries = []

    for field in fields:
        tk.Label(add_win, text=field, font=("Arial", 12), bg="#fefae0").pack(pady=5)
        entry = tk.Entry(add_win, font=("Arial", 12), width=40)
        entry.pack()
        entries.append(entry)

    def them_tu():
        japanese, romaji, meaning, topic = [e.get().strip() for e in entries]

        if not japanese or not meaning:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập ít nhất từ và nghĩa.")
            return

        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Words (japanese, romaji, meaning, topic) VALUES (?, ?, ?, ?)",
                       (japanese, romaji, meaning, topic))
        conn.commit()
        conn.close()

        messagebox.showinfo("Thành công", "Đã thêm từ mới thành công!")
        for e in entries:
            e.delete(0, tk.END)

    tk.Button(add_win, text="Thêm từ", font=("Arial", 12), bg="#27ae60", fg="white", command=them_tu).pack(pady=20)

    tk.Button(add_win, text="⬅ Quay lại menu", font=("Arial", 11), bg="#dfe6e9", command=lambda: (add_win.destroy(), show_vocab_lookup(user_name))).pack(pady=10)

    add_win.mainloop()
