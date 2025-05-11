
import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
from modules.menu import show_menu
from modules.db_helper import get_db_path

def show_alphabet_quiz(user_name):
    win = tk.Tk()
    win.title("Quiz bảng chữ cái")
    win.geometry("750x500")
    win.configure(bg="#f7f9fa")

    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win, 750, 500)

    tk.Label(win, text=f"🈶 {user_name}, hãy chọn đáp án đúng:", font=("Arial", 14), bg="#f7f9fa").pack(pady=20)

    def get_alphabet_data():
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()
        cursor.execute("SELECT hiragana, katakana, romaji FROM Alphabets")
        data = cursor.fetchall()
        conn.close()
        return data

    all_data = get_alphabet_data()
    random.shuffle(all_data)
    quiz_data = all_data[:20]  # lấy 20 câu ngẫu nhiên

    state = {
        "score": 0,
        "current_index": 0
    }

    def create_question():
        if state["current_index"] >= len(quiz_data):
            end_quiz()
            return None, None, None

        row = quiz_data[state["current_index"]]
        hira, kata, romaji = row

        current_num = state["current_index"] + 1
        total = len(quiz_data)

        # Ngẫu nhiên chọn loại ký tự: Hiragana hoặc Katakana
        char_type = random.choice(["hira", "kata"])
        if char_type == "hira":
            question_text = f'Câu {current_num}/{total}: "{romaji}" là ký tự Hiragana nào?'
            correct = hira
            wrongs = [r[0] for i, r in enumerate(quiz_data) if i != state["current_index"]]
        else:
            question_text = f'Câu {current_num}/{total}: "{romaji}" là ký tự Katakana nào?'
            correct = kata
            wrongs = [r[1] for i, r in enumerate(quiz_data) if i != state["current_index"]]

        wrong_answers = random.sample(wrongs, 3)
        options = [correct] + wrong_answers
        random.shuffle(options)

        return question_text, correct, options

    def check_answer(selected_option):
        disable_buttons()
        correct = current_data["correct"]

        if selected_option == correct:
            state["score"] += 1
            result_label.config(text="✅ Chính xác!", fg="green")
        else:
            result_label.config(text=f"❌ Sai! Đáp án đúng: {correct}", fg="red")

    def disable_buttons():
        for btn in option_buttons:
            btn.config(state="disabled")

    def enable_buttons():
        for btn in option_buttons:
            btn.config(state="normal")

    def next_question():
        result_label.config(text="")
        enable_buttons()
        question, correct_answer, options = create_question()
        if not question:
            return
        current_data["correct"] = correct_answer
        question_label.config(text=question)
        for i, option in enumerate(options):
            option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))
        state["current_index"] += 1

    def end_quiz():
        total_questions = len(quiz_data)
        correct = state["score"]
        messagebox.showinfo("🎉 Kết thúc", f"✔ Bạn đã hoàn thành quiz!\n"
                                           f"✅ Số câu đúng: {correct}/{total_questions}\n")
        win.destroy()
        show_menu(user_name)

    current_data = {"correct": None}

    question_label = tk.Label(win, text="", font=("Arial", 16), bg="#f7f9fa", wraplength=700)
    question_label.pack(pady=20)

    option_buttons = []
    for _ in range(4):
        btn = tk.Button(win, text="", font=("Arial", 14), bg="#dcdde1", width=20)
        btn.pack(pady=5)
        option_buttons.append(btn)

    result_label = tk.Label(win, text="", font=("Arial", 14), bg="#f7f9fa")
    result_label.pack(pady=10)

    next_button = tk.Button(win, text="👉 Câu tiếp theo", font=("Arial", 14), bg="#0984e3", fg="white", command=next_question)
    next_button.pack(pady=10)

    back_button = tk.Button(win, text="🔙 Quay lại menu", font=("Arial", 12), bg="#636e72", fg="white", command=lambda: [win.destroy(), show_menu(user_name)])
    back_button.pack(pady=10)

    next_question()
    win.mainloop()
