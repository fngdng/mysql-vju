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
    conn.close()

    index = [0]  # mutable index

    def update_display():
        if 0 <= index[0] < len(words):
            jp, romaji, vi = words[index[0]]
            word_label.config(text=f"Từ: {jp}\nRomaji: {romaji}\nNghĩa: {vi}")
            status_label.config(text=f"{index[0]+1}/{len(words)}")

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
