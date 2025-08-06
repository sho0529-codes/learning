import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("タイトル")  # ウィンドウのタイトルを設定

# 入力欄
# # 1行のみ
# entry = tk.Entry(root, width=100, height=3)  # 幅を指定
# entry.grid(row=0, column=0, columnspan=3)  # columnspanで横幅

# 複数行
text = tk.Text(root, width=100, height=10)  # 幅と高さを指定
text.grid(row=0, column=0, columnspan=3)

# 文字表示
label = tk.Label(root, text="ここに表示")
label.grid(row=1, column=0, columnspan=3)

# 入力欄の値を表示するボタン
def show_text():
    # label.config(text=entry.get())
    label.config(text=text.get("1.0", tk.END)) # 1.0はテキストの先頭、tk.ENDは最後まで
button = tk.Button(root, text="表示", command=show_text)
button.grid(row=2, column=0, columnspan=3)

# ボタンの位置を変える
# ボタンを行列で配置
button1 = tk.Button(root, text="ボタン1", command=lambda: print("ボタン1が押されました"), width=30, height=3)
button1.grid(row=3, column=0)
button2 = tk.Button(root, text="ボタン2", command=lambda: print("ボタン2が押されました"), width=30, height=3)
button2.grid(row=3, column=1)
button3 = tk.Button(root, text="ボタン3", command=lambda: print("ボタン3が押されました"), width=30, height=3)
button3.grid(row=3, column=2)
button4 = tk.Button(root, text="ボタン4", command=lambda: print("ボタン4が押されました"), width=30, height=3)
button4.grid(row=4, column=0)
button5 = tk.Button(root, text="ボタン5", command=lambda: print("ボタン5が押されました"), width=30, height=3)
button5.grid(row=4, column=1)
button6 = tk.Button(root, text="ボタン6", command=lambda: print("ボタン6が押されました"), width=30, height=3)
button6.grid(row=4, column=2)

# メインループ
root.mainloop()