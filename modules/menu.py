def show_menu(user_name):
    import tkinter as tk
    from modules.vocab_lookup import show_vocab_lookup
    from modules.quiz import show_quiz
    from modules.choose_topic import show_topic_selection
    from modules.alphabet import show_alphabet
    from modules.progress_tracker import show_progress
    from modules.word_history_ui import show_word_history
    from modules.quiz_alphabet import show_alphabet_quiz



    menu = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(menu, 800, 750)
    menu.title("Chức năng chính")
    menu.geometry("800x700")
    menu.configure(bg="#fff8f0")

    tk.Label(menu, text=f"🌟 Xin chào {user_name}, hãy chọn chức năng:", font=("Arial", 20, "bold"), bg="#fff8f0", fg="#2d3436").pack(pady=30)

    tk.Button(menu, text="🔍 Tra từ vựng", font=("Arial", 14), bg="#74b9ff", fg="white", padx=10, pady=5,
              command=lambda: (menu.destroy(), show_vocab_lookup(user_name))).pack(pady=10)
    tk.Button(menu, text="📖 Bảng chữ cái", font=("Arial", 14), bg="#fab1a0", fg="black", padx=10, pady=5,
              command=lambda: (menu.destroy(), show_alphabet(user_name))).pack(pady=10)
    tk.Button(menu, text="📝 Làm bài quiz", font=("Arial", 14), bg="#55efc4", fg="black", padx=10, pady=5,
              command=lambda: (menu.destroy(), show_quiz(user_name))).pack(pady=10)
    tk.Button(menu, text="📝 Làm quiz chữ cái", font=("Arial", 14), bg="#55efc4", fg="black", padx=10, pady=5,
              command=lambda: (menu.destroy(), show_alphabet_quiz(user_name))).pack(pady=10)
    tk.Button(menu, text="📚 Học từ vựng theo chủ đề", font=("Arial", 14), bg="#81ecec", fg="black", padx=10, pady=5,
          command=lambda: (menu.destroy(), show_topic_selection(user_name))).pack(pady=10)
    
    tk.Button(menu, text="🕘 Lịch sử học từ", font=("Arial", 14), bg="#dcdde1", fg="black", padx=10, pady=5,
          command=lambda: (menu.destroy(), show_word_history(user_name))).pack(pady=10)

    tk.Button(menu, text="📈 Xem tiến độ học tập", font=("Arial", 14), bg="#ffeaa7", fg="black", padx=10, pady=5,
          command=lambda: (menu.destroy(), show_progress(user_name))).pack(pady=10)

    tk.Button(menu, text="🔙 Quay lại trang chủ", font=("Arial", 12), bg="#dfe6e9", command=lambda: (menu.destroy(), __import__('modules.homepage').homepage.show_homepage(user_name))).pack(pady=40)

    menu.mainloop()