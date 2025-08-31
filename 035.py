# osでフォルダの中身を取得

import os

folder_path = None # 現在地を見るなら無しで良い
# folder_path = "learning" # 普通は相対パスか絶対パス

def show_lst(lst):
    char = ""
    for i in lst:
        char += str(i) + "\n"
    
    return char

def show_sorted_lst(lst):
    code = ""
    text = ""
    other = ""
    for i in lst:
        if i[-3:] == ".py":
            code += f"  {str(i)}\n"
        elif i[-4:] == ".txt":
            text += f"  {str(i)}\n"
        else:
            other += f"  {str(i)}\n"

    return f"code:\n{code}\ntext:\n{text}\nother\n{other}"

lst = os.listdir(folder_path)
# for i in lst:
#     print(i, type(i))

# print(lst)
# print(show_lst(lst))
print(show_sorted_lst(lst))

