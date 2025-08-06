import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("タイトル")  # ウィンドウのタイトルを設定

# 入力欄
entry = tk.Entry(root)
entry.pack()

# 文字表示
label = tk.Label(root, text="ここに表示")
label.pack()

# 入力欄の値を表示するボタン
def show_text():
    label.config(text=entry.get())
button = tk.Button(root, text="表示", command=show_text)
button.pack()

# ボタンの位置を変える
# # ボタンを左側に配置
# button1 = tk.Button(root, text="ボタン1", command=lambda: print("ボタン1が押されました"))
# button1.pack(side=tk.LEFT)
# button2 = tk.Button(root, text="ボタン2", command=lambda: print("ボタン2が押されました"))
# button2.pack(side=tk.LEFT)
# button3 = tk.Button(root, text="ボタン3", command=lambda: print("ボタン3が押されました"))
# button3.pack(side=tk.LEFT)

# # ボタンを右側に配置
# button4 = tk.Button(root, text="ボタン4", command=lambda: print("ボタン4が押されました"))
# button4.pack(side=tk.RIGHT)
# button5 = tk.Button(root, text="ボタン5", command=lambda: print("ボタン5が押されました"))
# button5.pack(side=tk.RIGHT)
# button6 = tk.Button(root, text="ボタン6", command=lambda: print("ボタン6が押されました"))
# button6.pack(side=tk.RIGHT)

# # ボタンを下側に配置
# button7 = tk.Button(root, text="ボタン7", command=lambda: print("ボタン7が押されました"))
# button7.pack(side=tk.BOTTOM)
# button8 = tk.Button(root, text="ボタン8", command=lambda: print("ボタン8が押されました"))
# button8.pack(side=tk.BOTTOM)
# button9 = tk.Button(root, text="ボタン9", command=lambda: print("ボタン9が押されました"))
# button9.pack(side=tk.BOTTOM)

# メインループ
root.mainloop()