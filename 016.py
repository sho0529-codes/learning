# 複数ページを作れないかやってみる

import tkinter as tk

root = tk.Tk()
root.title("複数ページのサンプル")

# シーン切り替え用のフレーム
current_frame = None

def show_scene(frame_func):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()  # 前のシーンを消す
    current_frame = frame_func()

def scene1():
    frame = tk.Frame(root)  # 新しいフレームを作成、以下に内容
    label = tk.Label(frame, text="シーン1")  # 文字
    label.pack()
    button1 = tk.Button(frame, text="次へ", command=lambda: show_scene(scene2), width = 10)  # ボタン
    button1.pack()
    text = tk.Text(frame, width=10, height=1)  # テキスト入力欄
    text.pack()
    button2 = tk.Button(frame, text="入力内容を表示", command=lambda: print(text.get("1.0", tk.END)), width = 10)
    button2.pack()
    frame.pack()  # フレームを表示
    return frame

def scene2():
    frame = tk.Frame(root)
    label = tk.Label(frame, text="シーン2")
    label.pack()
    button = tk.Button(frame, text="戻る", command=lambda: show_scene(scene1), width = 10)
    button.pack()
    text = tk.Text(frame, width=10, height=1)  # テキスト入力欄
    text.pack()
    button2 = tk.Button(frame, text="入力内容を表示", command=lambda: print(text.get("1.0", tk.END)), width = 10)
    button2.pack()
    frame.pack()
    return frame

show_scene(scene1)  # 最初のシーンを表示

root.mainloop()