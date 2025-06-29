# 正規表現のまとめ
# 毎回細かいとこ忘れる

"""
「.」
・任意の一文字
・「abc」が「a..」みたいな

「^」
・行の先頭
・「^hello」が「hello python」とか

「$」
・行の末尾
・「python$」が「hello pyton」

「*」
・直前の文字の0回以上の繰り返し
・「no*」が「n」とか「no」とか「noooooooooooo」とか

「+」
・直前の文字の1回以上の繰り返し
・「no+」が「no」とか「nooo」とか

「?」
・直前の文字の0回または1回繰り返し
「no?」が「n」とか「no」

「[]」
・[]内の文字のどれか
・[aiueo]でaiueoのどれか1文字みたいな

「[^]」
・[]の内の指定が否定に変わる
・[^aiueo]でaiueo以外の1文字みたいな

「{n}」
・直前の文字をn回繰り替えし
・「no{3}」で「nooo」

「{n, m}」
・直前の文字をn回以上m回以下繰り返し
・「no{1, 12}」で「no」とか「noooooo」とか「noooooooooooo」

「|」
・orみたいなやつ
・「python|java」で「python」か「java」みたいな

「()」
・()内の文字を1つとして扱う
・「python+」が「pythonnn」に対して、「(python)+」が「pythonpythonpython」みたいな

"""