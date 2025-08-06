import tkinter as tk

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
button = tk.Button(root, text="押してね", command= lambda: print("ボタンが押されました"))
button.pack()

x = 0
def push_button():
    global x
    x += 1
    print(f"xの値: {x}")
button2 = tk.Button(root, text="x", command=push_button)
button2.pack()

# ウィンドウを表示し続ける
root.mainloop()