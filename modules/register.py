import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
from modules.db_helper import get_db_path


def register_window():
    def register():
        name = entry_name.get().strip()
        email = entry_email.get().strip()
        password = entry_password.get().strip()
        birthday = entry_birthday.get().strip()

        if not name or not email or not password or not birthday:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng điền đầy đủ thông tin.")
            return

        if not re.match(r"^[A-Za-zÀ-ỹ\s]+$", name):
            messagebox.showerror("Lỗi tên", "Tên chỉ được chứa chữ cái và khoảng trắng!")
            return

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            messagebox.showerror("Lỗi email", "Email không đúng định dạng!")
            return

        if len(password) < 5:
            messagebox.showerror("Lỗi mật khẩu", "Mật khẩu phải có ít nhất 5 ký tự!")
            return

        if not re.match(r'^\d{2}/\d{2}/\d{4}$', birthday):
            messagebox.showerror("Lỗi ngày sinh", "Ngày sinh phải theo định dạng dd/mm/yyyy (VD: 01/01/2005)")
            return

        try:
            conn = sqlite3.connect(get_db_path())
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

    def go_back_login():
        register_win.destroy()
        from modules.login import login_window
        login_window()

    register_win = tk.Tk()

    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")

    center_window(register_win, 600, 500)
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

    tk.Label(register_win, text="Ngày sinh (dd/mm/yyyy)", font=("Arial", 12)).pack()
    entry_birthday = tk.Entry(register_win, font=("Arial", 12))
    entry_birthday.pack(pady=10)

    tk.Button(register_win, text="Đăng ký", command=register, bg="black", fg="white", font=("Arial", 12), width=20).pack(pady=20)

    tk.Button(register_win, text="⬅ Đã có tài khoản? Quay lại đăng nhập", font=("Arial", 11), bg="#dfe6e9", command=go_back_login).pack(pady=10)

    register_win.mainloop()
