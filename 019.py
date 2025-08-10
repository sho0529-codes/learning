import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("メモ帳っぽいなにか")
input_text = ""
output_file = "learning/019_output.txt"

# 文字表示1
label1 = tk.Label(root, text="下に文章")
label1.pack()

# 入力欄
text = tk.Text(root, width=100)
text.pack()

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