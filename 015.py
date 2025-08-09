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
    button = tk.Button(frame, text="次へ", command=lambda: show_scene(scene2))  # ボタン
    button.pack()
    frame.pack()  # フレームを表示
    return frame

def scene2():
    frame = tk.Frame(root)
    label = tk.Label(frame, text="シーン2")
    label.pack()
    button = tk.Button(frame, text="戻る", command=lambda: show_scene(scene1))
    button.pack()
    frame.pack()
    return frame

show_scene(scene1)  # 最初のシーンを表示

root.mainloop()