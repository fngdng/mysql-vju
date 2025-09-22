import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
from modules.menu import show_menu
from modules.db_helper import get_db_path

def show_quiz(user_name):
    def open_mode_selection():
        mode_win = tk.Tk()

        def center_window(win, width, height):
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            x = int((screen_width / 2) - (width / 2))
            y = int((screen_height / 2) - (height / 2))
            win.geometry(f"{width}x{height}+{x}+{y}")
        center_window(mode_win, 750, 500)
        mode_win.title("Chọn chế độ quiz")
        mode_win.configure(bg="#f7f9fa")

        tk.Label(mode_win, text=f"🎓 Xin chào {user_name}, chọn chế độ:", font=("Arial", 14), bg="#f7f9fa").pack(pady=20)

        tk.Button(mode_win, text="📘 Nghĩa ➜ Japanese", font=("Arial", 12), width=25,
                  command=lambda: [mode_win.destroy(), show_quiz_meaning_to_japanese(user_name)]).pack(pady=5)

        tk.Button(mode_win, text="📗 Japanese ➜ Nghĩa", font=("Arial", 12), width=25,
                  command=lambda: [mode_win.destroy(), show_quiz_japanese_to_meaning(user_name)]).pack(pady=5)

        tk.Button(mode_win, text="🔙 Quay lại menu", font=("Arial", 10),
                  command=lambda: [mode_win.destroy(), show_menu(user_name)]).pack(pady=10)

        mode_win.mainloop()

    open_mode_selection()

def show_quiz_meaning_to_japanese(user_name):
    run_quiz(user_name, mode="meaning_to_japanese")

def show_quiz_japanese_to_meaning(user_name):
    run_quiz(user_name, mode="japanese_to_meaning")

def run_quiz(user_name, mode="japanese_to_meaning"):
    win = tk.Tk()

    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win, 750, 500)

    win.title("Làm bài quiz")
    win.configure(bg="#f7f9fa")

    tk.Label(win, text=f"🔍 {user_name}, hãy chọn đáp án đúng:", font=("Arial", 14), bg="#f7f9fa").pack(pady=20)

    def get_quiz_data():
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()
        cursor.execute("SELECT japanese, romaji, meaning FROM Words WHERE japanese IS NOT NULL AND romaji IS NOT NULL AND meaning IS NOT NULL")
        data = cursor.fetchall()
        conn.close()
        return [row for row in data if all(row)]

    all_data = get_quiz_data()
    random.shuffle(all_data)
    quiz_data = all_data[:15]

    state = {
        "score": 0,
        "current_index": -1,
        "answered": True  # Cho phép hiển thị câu đầu
    }

    current_data = {"correct": None}

    def create_question():
        if state["current_index"] >= len(quiz_data) - 1:
            end_quiz()
            return None, None, None

        state["current_index"] += 1

        row = quiz_data[state["current_index"]]
        japanese, romaji, meaning = row

        current_num = state["current_index"] + 1
        total = len(quiz_data)

        if mode == "meaning_to_japanese":
            question_text = f"Câu {current_num}/{total}: \"{meaning}\" là từ nào sau đây?"
            correct = f"{japanese} ({romaji})"
            wrongs = [f"{r[0]} ({r[1]})" for i, r in enumerate(quiz_data) if i != state["current_index"]]
        else:
            question_text = f"Câu {current_num}/{total}: Từ \"{japanese}\" (romaji: {romaji}) có nghĩa là gì?"
            correct = meaning
            wrongs = [r[2] for i, r in enumerate(quiz_data) if i != state["current_index"]]

        wrong_answers = random.sample(wrongs, 3)
        options = [correct] + wrong_answers
        random.shuffle(options)

        return question_text, correct, options

    def check_answer(selected_option):
        if state["answered"]:
            return

        disable_buttons()
        state["answered"] = True

        correct = current_data["correct"]
        current_row = quiz_data[state["current_index"]]
        japanese, romaji, meaning = current_row

        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM Users WHERE name = ?", (user_name,))
        user = cursor.fetchone()
        user_email = user[0] if user else None

        cursor.execute("SELECT id FROM Words WHERE japanese = ? AND romaji = ? AND meaning = ?",
                       (japanese, romaji, meaning))
        word = cursor.fetchone()
        word_id = word[0] if word else None

        from datetime import datetime
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if user_email and word_id:
            cursor.execute("SELECT id FROM Progress WHERE user_email = ? AND word_id = ?", (user_email, word_id))
            existing = cursor.fetchone()
            if existing:
                if selected_option == correct:
                    cursor.execute("UPDATE Progress SET correct = correct + 1, last_practiced = ? WHERE user_email = ? AND word_id = ?", (now, user_email, word_id))
                else:
                    cursor.execute("UPDATE Progress SET incorrect = incorrect + 1, last_practiced = ? WHERE user_email = ? AND word_id = ?", (now, user_email, word_id))
            else:
                cursor.execute("INSERT INTO Progress (user_email, word_id, correct, incorrect, last_practiced) VALUES (?, ?, ?, ?, ?)",
                               (user_email, word_id,
                                1 if selected_option == correct else 0,
                                0 if selected_option == correct else 1,
                                now))
        conn.commit()
        conn.close()

        if selected_option == correct:
            state["score"] += 1
            result_label.config(text="✅ Đúng!", fg="green")
        else:
            result_label.config(text=f"❌ Sai! Đáp án đúng: {correct}", fg="red")

    def disable_buttons():
        for btn in option_buttons:
            btn.config(state="disabled")

    def enable_buttons():
        for btn in option_buttons:
            btn.config(state="normal")

    def next_question():
        if not state["answered"]:
            messagebox.showwarning("⚠️ Cảnh báo", "Vui lòng chọn một đáp án trước khi tiếp tục.")
            return

        state["answered"] = False
        result_label.config(text="")
        enable_buttons()

        question, correct_answer, options = create_question()
        if not question:
            return
        current_data["correct"] = correct_answer
        question_label.config(text=question)
        for i, option in enumerate(options):
            option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

    def end_quiz():
        total_questions = len(quiz_data)
        correct = state["score"]
        messagebox.showinfo("🎉 Kết thúc", f"✔ Bạn đã hoàn thành quiz!\n"
                                           f"✅ Số câu đúng: {correct}/{total_questions}\n")
        win.destroy()
        show_menu(user_name)

    question_label = tk.Label(win, text="", font=("Arial", 16), bg="#f7f9fa", wraplength=700)
    question_label.pack(pady=20)

    option_buttons = []
    for _ in range(4):
        btn = tk.Button(win, text="", font=("Arial", 14), bg="#e0e0e0", width=30)
        btn.pack(pady=5)
        option_buttons.append(btn)

    result_label = tk.Label(win, text="", font=("Arial", 14), bg="#f7f9fa")
    result_label.pack(pady=10)

    next_button = tk.Button(win, text="👉 Câu tiếp theo", font=("Arial", 14), bg="#4caf50", fg="white", command=next_question)
    next_button.pack(pady=10)

    back_button = tk.Button(win, text="🔙 Quay lại menu", font=("Arial", 12), bg="#e53935", fg="white", command=lambda: [win.destroy(), show_menu(user_name)])
    back_button.pack(pady=10)

    next_question()
    win.mainloop()