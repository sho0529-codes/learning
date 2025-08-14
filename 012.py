import tkinter as tk
from tkinter import ttk

# ウィンドウの作成
root = tk.Tk()  # ウィンドウ（Tkクラスのインスタンス）を作成
root.title("タイトル")  # ウィンドウのタイトルを設定

# 文字表示
label = tk.Label(root, text="こんにちは")
label.pack()  # ウィンドウに配置

# 入力欄
entry = tk.Entry(root)
entry.pack()
print("入力欄の値:", entry.get())  # 初期状態では空

# ボタン
button1 = tk.Button(root, text="押してね", command= lambda: print("ボタンが押されました"))
button1.pack()

x = 0
def push_button():
    global x
    x += 1
    print(f"xの値: {x}")
button2 = tk.Button(root, text="x", command=push_button)
button2.pack()

# プルダウン（OptionMenu）
options = ["選択肢A", "選択肢B", "選択肢C"]
selected = tk.StringVar()
selected.set(options[0])  # 初期値
option_menu = tk.OptionMenu(root, selected, *options)
option_menu.pack()

def show_selected():
    print("選択された値:", selected.get())
button3 = tk.Button(root, text="表示", command=show_selected)
button3.pack()

# プルダウン（Combobox）
options = ["選択肢A", "選択肢B", "選択肢C"]
combo = ttk.Combobox(root, values=options)
combo.set(options[0])  # 初期値
combo.pack()

def show_selected():
    print("選択された値:", combo.get())
button4 = tk.Button(root, text="表示", command=show_selected)
button4.pack()

# メニューバーの作成
menu_bar = tk.Menu(root)

# ファイルメニューの作成と配置
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="新規", command=lambda: print("新規"))
file_menu.add_command(label="開く", command=lambda: print("開く"))
file_menu.add_separator()  # 薄い横線
file_menu.add_command(label="終了", command=root.quit)  # root.quitで終了処理
menu_bar.add_cascade(label="ファイル", menu=file_menu)  # ここで設定終了

# 編集メニューの作成と配置
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="切り取り", command=lambda: print("切り取り"))
edit_menu.add_command(label="コピー", command=lambda: print("コピー"))
edit_menu.add_command(label="貼り付け", command=lambda: print("貼り付け"))
menu_bar.add_cascade(label="編集", menu=edit_menu)

# メニューバーの設定
root.config(menu=menu_bar)

# ウィンドウを表示し続ける
root.mainloop()