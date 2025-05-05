def show_homepage(user_name):
    import tkinter as tk
    from modules.login import login_window

    def open_feature_selection():
        home.destroy()
        from modules.menu import show_menu
        show_menu(user_name)

    home = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(home, 900, 600)    
    home.title("Trang chủ")
    home.geometry("900x600")
    home.configure(bg="#f0f4f7")

    title_font = ("Helvetica", 24, "bold")
    subtitle_font = ("Segoe UI", 14)

    welcome = tk.Label(
        home,
        text=f"👋 Xin chào, {user_name}!",
        font=title_font,
        fg="#2c3e50",
        bg="#f0f4f7"
    )
    welcome.pack(pady=40)

    subtitle = tk.Label(
        home,
        text="Chào mừng bạn đến với ứng dụng học tiếng Nhật",
        font=subtitle_font,
        fg="#34495e",
        bg="#f0f4f7"
    )
    subtitle.pack(pady=10)

    description = tk.Label(
        home,
        text="Hãy bắt đầu hành trình học từ vựng, làm quiz và theo dõi tiến độ của bạn.",
        font=("Segoe UI", 12),
        fg="#555",
        bg="#f0f4f7"
    )
    description.pack(pady=20)

    btn_start = tk.Button(
        home,
        text="Vào học",
        font=("Arial", 14, "bold"),
        bg="#2980b9",
        fg="white",
        padx=20,
        pady=10,
        relief="flat",
        command=open_feature_selection
    )
    btn_start.pack(pady=30)

    btn_logout = tk.Button(
        home,
        text="Đăng xuất",
        font=("Arial", 12),
        bg="#e74c3c",
        fg="white",
        padx=10,
        pady=5,
        command=lambda: (home.destroy(), login_window())
    )
    btn_logout.pack(pady=10)

    home.mainloop()