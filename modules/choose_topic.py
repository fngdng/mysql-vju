def show_topic_selection(user_name):
    import tkinter as tk
    import sqlite3
    from tkinter import ttk
    from tkinter import messagebox
    from modules.menu import show_menu
    from modules.topic_word import show_words_by_topic
    from modules.db_helper import get_db_path

    def load_words_by_topic(selected_topic):
        if not selected_topic:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một chủ đề")
            return

        win.destroy()
        show_words_by_topic(user_name, selected_topic)

    win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win, 500, 350)    
    win.title("Chọn chủ đề từ vựng")
    win.geometry("500x350")
    win.configure(bg="#fef9e7")

    tk.Label(win, text=f"📚 Xin chào {user_name}!\nChọn một chủ đề để học từ vựng", font=("Arial", 14, "bold"), bg="#fef9e7", justify="center").pack(pady=20)

    # Lấy danh sách chủ đề từ DB
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT topic FROM Words WHERE topic IS NOT NULL AND topic != ''")
    topics = [row[0] for row in cursor.fetchall()]
    conn.close()

    topic_var = tk.StringVar()
    topic_combo = ttk.Combobox(win, textvariable=topic_var, values=topics, font=("Arial", 12), state="readonly")
    topic_combo.pack(pady=10)

    if topics:
        topic_combo.current(0)

    tk.Button(win, text="Bắt đầu học", font=("Arial", 12), bg="#58d68d", fg="white",
              command=lambda: load_words_by_topic(topic_var.get())).pack(pady=20)

    tk.Button(win, text="⬅ Quay lại menu", font=("Arial", 11), bg="#dfe6e9",
              command=lambda: (win.destroy(), show_menu(user_name))).pack(pady=10)

    win.mainloop()