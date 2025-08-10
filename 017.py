# Flaskの最小サンプル
from flask import Flask

# インスタンス変数？の作成
app = Flask(__name__)

@app.route("/")  # トップページのとき、javaに書き方なかったっけ
def hello():
    return "Hello, Flask!"

app.run(debug=True)  # webサーバー？の起動