import tkinter as tk
from tkinter import ttk

# ウィンドウの作成
root = tk.Tk()
root.title("メモ帳っぽいなにか")
input_text = ""
output_file = "learning/020_output.txt"

# 文字表示1
label1 = tk.Label(root, text="下に文章")
label1.pack()

# 入力欄
text = tk.Text(root, width=100)
text.pack()

def insert_template(template):
    text.insert(tk.INSERT, template)
ttk_button = tk.Button(root, text="ショートカット", command=lambda: insert_template("ショートカット"))
ttk_button.pack(side=tk.LEFT)

# 入力内容
def push_button():
    # テキストを表示
    global input_text
    input_text = text.get("1.0", tk.END)
    print(input_text)  # デバッグ用
    label2.config(text=input_text)  # label2のテキストを更新、これ無いと反映されない

    # .txtに保存
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(input_text)
        print(".txtに保存")  # デバッグ用

button = tk.Button(root, text="完了", command=push_button)
button.pack()

# 文字表示2
label2 = tk.Label(root, text="ここに入力内容")
label2.pack()

# メインループ
root.mainloop()