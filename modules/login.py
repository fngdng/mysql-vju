import tkinter as tk
from tkinter import messagebox
import sqlite3
from modules.homepage import show_homepage


def login_window():
    def login():
        email = entry_email.get()
        password = entry_password.get()

        conn = sqlite3.connect("./DB/japanese.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM Users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            login_win.destroy()
            show_homepage(user[0])
        else:
            messagebox.showerror("Lỗi", "Email hoặc mật khẩu không đúng!")

    def open_register():
        login_win.destroy()
        from modules.register import register_window
        register_window()

    login_win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(login_win, 600, 500)
    login_win.title("Đăng nhập")
    login_win.geometry("600x500")

    tk.Label(login_win, text="Đăng nhập", font=("Arial", 24, "bold")).pack(pady=30)

    tk.Label(login_win, text="Email", font=("Arial", 12)).pack()
    entry_email = tk.Entry(login_win, font=("Arial", 12))
    entry_email.pack(pady=10)

    tk.Label(login_win, text="Mật khẩu", font=("Arial", 12)).pack()
    entry_password = tk.Entry(login_win, show="*", font=("Arial", 12))
    entry_password.pack(pady=10)

    tk.Button(login_win, text="Đăng nhập", command=login, bg="black", fg="white", font=("Arial", 12), width=20).pack(pady=20)
    tk.Button(login_win, text="Chưa có tài khoản? Đăng ký", command=open_register, font=("Arial", 10)).pack()

    login_win.mainloop()
