# 入力されたテキストから特定の文字を取り除く

def extract_char(text: str, chars: list) -> str:
    """
    引き数：text（入力するテキスト）, chars（取り除く文字のリスト）
    返り値：text（特定の文字を取り除いたテキスト）
    """
    for char in chars:
        text = text.replace(char, "")

    return text

def read_file(file_path: str) -> str:
    """
    引き数：file_path（読み込むファイルのパス）
    返り値：text（読み込んだテキスト）
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return text

# print(text)
text = read_file("README.md")  # 読み込むファイルのパスを指定
lst = ["### ", "## ", "# ", "- ", " "]  # 「#」は多い順で指定して、空白まで含めた方が良いっぽい
print(extract_char(text, lst))