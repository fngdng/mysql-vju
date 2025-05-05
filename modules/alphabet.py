def show_alphabet():
    import tkinter as tk
    from modules.menu import show_menu

    hiragana = [
        ["あ", "い", "う", "え", "お"],
        ["か", "き", "く", "け", "こ"],
        ["さ", "し", "す", "せ", "そ"],
        ["た", "ち", "つ", "て", "と"],
        ["な", "に", "ぬ", "ね", "の"],
        ["は", "ひ", "ふ", "へ", "ほ"],
        ["ま", "み", "む", "め", "も"],
        ["や", "", "ゆ", "", "よ"],
        ["ら", "り", "る", "れ", "ろ"],
        ["わ", "", "を", "", "ん"]
    ]

    katakana = [
        ["ア", "イ", "ウ", "エ", "オ"],
        ["カ", "キ", "ク", "ケ", "コ"],
        ["サ", "シ", "ス", "セ", "ソ"],
        ["タ", "チ", "ツ", "テ", "ト"],
        ["ナ", "ニ", "ヌ", "ネ", "ノ"],
        ["ハ", "ヒ", "フ", "ヘ", "ホ"],
        ["マ", "ミ", "ム", "メ", "モ"],
        ["ヤ", "", "ユ", "", "ヨ"],
        ["ラ", "リ", "ル", "レ", "ロ"],
        ["ワ", "", "ヲ", "", "ン"]
    ]

    def hien_bang(ky_tu):
        for widget in bang_frame.winfo_children():
            widget.destroy()

        data = hiragana if ky_tu == "hira" else katakana
        romaji = [
            ["a", "i", "u", "e", "o"],
            ["ka", "ki", "ku", "ke", "ko"],
            ["sa", "shi", "su", "se", "so"],
            ["ta", "chi", "tsu", "te", "to"],
            ["na", "ni", "nu", "ne", "no"],
            ["ha", "hi", "fu", "he", "ho"],
            ["ma", "mi", "mu", "me", "mo"],
            ["ya", "", "yu", "", "yo"],
            ["ra", "ri", "ru", "re", "ro"],
            ["wa", "", "wo", "", "n"]
        ]

        for i, row in enumerate(data):
            for j, char in enumerate(row):
                romaji_text = romaji[i][j]
                display = f"{char}\n{romaji_text}" if char else ""
                tk.Label(bang_frame, text=display, font=("Arial", 10), width=6, height=2, bg="#ffffff", relief="ridge").grid(row=i, column=j, padx=4, pady=4)

    win = tk.Tk()
    def center_window(win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        win.geometry(f"{width}x{height}+{x}+{y}")
    center_window(win, 550, 680)    
    win.title("Bảng chữ cái tiếng Nhật")
    win.geometry("550x680")
    win.configure(bg="#ecf0f1")

    tk.Label(win, text="🔤 Bảng chữ cái tiếng Nhật", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

    nut_frame = tk.Frame(win, bg="#ecf0f1")
    tk.Button(nut_frame, text="Hiragana", font=("Arial", 12), bg="#74b9ff", command=lambda: hien_bang("hira")).pack(side="left", padx=10)
    tk.Button(nut_frame, text="Katakana", font=("Arial", 12), bg="#a29bfe", command=lambda: hien_bang("kata")).pack(side="left", padx=10)
    nut_frame.pack(pady=10)

    bang_frame = tk.Frame(win, bg="#ecf0f1")
    bang_frame.pack()

    hien_bang("hira")  # mặc định hiển thị bảng hiragana

    tk.Button(win, text="⬅ Quay lại menu", font=("Arial", 11), bg="#dfe6e9", command=lambda: (win.destroy(), show_menu("User"))).pack(pady=10)

    win.mainloop()