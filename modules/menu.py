def show_menu(user_name):
    import tkinter as tk
    from modules.vocab_lookup import show_vocab_lookup

    menu = tk.Tk()
    menu.title("Chức năng chính")
    menu.geometry("800x500")
    menu.configure(bg="#fff8f0")

    tk.Label(menu, text=f"🌟 Xin chào {user_name}, hãy chọn chức năng:", font=("Arial", 20, "bold"), bg="#fff8f0", fg="#2d3436").pack(pady=30)

    tk.Button(menu, text="🔍 Tra từ vựng", font=("Arial", 14), bg="#74b9ff", fg="white", padx=10, pady=5,
              command=lambda: (menu.destroy(), show_vocab_lookup(user_name))).pack(pady=10)
    tk.Button(menu, text="📝 Làm bài quiz", font=("Arial", 14), bg="#55efc4", fg="black", padx=10, pady=5).pack(pady=10)
    tk.Button(menu, text="📈 Xem tiến độ học tập", font=("Arial", 14), bg="#ffeaa7", fg="black", padx=10, pady=5).pack(pady=10)

    tk.Button(menu, text="🔙 Quay lại trang chủ", font=("Arial", 12), bg="#dfe6e9", command=lambda: (menu.destroy(), __import__('modules.homepage').homepage.show_homepage(user_name))).pack(pady=40)

    menu.mainloop()