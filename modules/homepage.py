def show_homepage(user_name):
    import tkinter as tk
    from modules.login import login_window

    home = tk.Tk()
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
        text="Bắt đầu học",
        font=("Arial", 14, "bold"),
        bg="#27ae60",
        fg="white",
        padx=20,
        pady=10,
        relief="flat"
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
