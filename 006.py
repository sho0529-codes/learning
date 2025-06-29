# 正規表現のまとめ
# 毎回細かいとこ忘れる
# 検出のテンプレprint(True if re.match("", "") else False)

import re

"""
「.」
・任意の一文字
・「abc」が「a..」みたいな
"""
print("\n" + ".")
print(("ab.", "abc"), True if re.match("ab.", "abc") else False)
print(("ab.", "abcd"), True if re.match("ab.", "abcd") else False)
print(("ab.", "ab"), True if re.match("ab.", "ab") else False)


"""
「^」
・行の先頭
・「^hello」が「hello python」とか

"""

print("\n" + "^")
print(("^hello", "hello python"), True if re.match("^hello", "hello python") else False)
print(("^hello", "hello world"), True if re.match("^hello", "hello world") else False)
print(("^python", "hello python"), True if re.match("^python", "hello python") else False)
print(("^hello", "say hello or good morning"), True if re.match("^hello", "say hello or good morning") else False)


"""

「$」
・行の末尾
・「python$」が「hello pyton」

"""

print("\n" + "$")
print(("python$", "hello python"), True if re.match("python$", "hello python") else False)
print(("hello$", "hello python"), True if re.match("hello$", "hello python") else False)

"""

「*」
・直前の文字の0回以上の繰り返し
・「no*」が「n」とか「no」とか「noooooooooooo」とか

"""

print("\n" + "*")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「+」
・直前の文字の1回以上の繰り返し
・「no+」が「no」とか「nooo」とか

"""

print("\n" + "+")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「?」
・直前の文字の0回または1回繰り返し
「no?」が「n」とか「no」

"""

print("\n" + "?")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「[]」
・[]内の文字のどれか
・[aiueo]でaiueoのどれか1文字みたいな

"""

print("\n" + "[]")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「[^]」
・[]の内の指定が否定に変わる
・[^aiueo]でaiueo以外の1文字みたいな

"""

print("\n" + "[^]")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「{n}」
・直前の文字をn回繰り替えし
・「no{3}」で「nooo」

"""

print("\n" + "{n}")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「{n, m}」
・直前の文字をn回以上m回以下繰り返し
・「no{1, 12}」で「no」とか「noooooo」とか「noooooooooooo」

"""

print("\n" + "{n, m}")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「|」
・orみたいなやつ
・「python|java」で「python」か「java」みたいな

"""

print("\n" + "|")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)

"""

「()」
・()内の文字を1つとして扱う
・「python+」が「pythonnn」に対して、「(python)+」が「pythonpythonpython」みたいな

"""

print("\n" + "()")
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)
print(True if re.match("", "") else False)