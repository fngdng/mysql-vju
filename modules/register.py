import tkinter as tk
from tkinter import messagebox
import sqlite3
# Không import login_window ở đầu file nữa để tránh vòng lặp


def register_window():
    def register():
        name = entry_name.get()
        email = entry_email.get()
        password = entry_password.get()
        birthday = entry_birthday.get()

        if not name or not email or not password:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng điền đầy đủ thông tin.")
            return

        try:
            conn = sqlite3.connect("D:/Japanese_learning_app/japanese.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Users (name, email, password, birthday)
                VALUES (?, ?, ?, ?)
            """, (name, email, password, birthday))
            conn.commit()
            conn.close()

            messagebox.showinfo("Thành công", "Đăng ký thành công! Quay lại đăng nhập.")
            register_win.destroy()
            from modules.login import login_window
            login_window()

        except sqlite3.IntegrityError:
            messagebox.showerror("Lỗi", "Email đã tồn tại!")

    register_win = tk.Tk()
    register_win.title("Đăng ký")
    register_win.geometry("600x500")

    tk.Label(register_win, text="Tạo tài khoản mới", font=("Arial", 24, "bold")).pack(pady=30)

    tk.Label(register_win, text="Tên", font=("Arial", 12)).pack()
    entry_name = tk.Entry(register_win, font=("Arial", 12))
    entry_name.pack(pady=10)

    tk.Label(register_win, text="Email", font=("Arial", 12)).pack()
    entry_email = tk.Entry(register_win, font=("Arial", 12))
    entry_email.pack(pady=10)

    tk.Label(register_win, text="Mật khẩu", font=("Arial", 12)).pack()
    entry_password = tk.Entry(register_win, show="*", font=("Arial", 12))
    entry_password.pack(pady=10)

    tk.Label(register_win, text="Ngày sinh", font=("Arial", 12)).pack()
    entry_birthday = tk.Entry(register_win, font=("Arial", 12))
    entry_birthday.pack(pady=10)

    tk.Button(register_win, text="Đăng ký", command=register, bg="black", fg="white", font=("Arial", 12), width=20).pack(pady=20)

    register_win.mainloop()