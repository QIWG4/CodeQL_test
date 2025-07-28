import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# --- 脆弱性を含むコード ---

# CWE-798: ハードコードされた認証情報
API_KEY = "my_super_secret_api_key_123" # 脆弱性: APIキーがハードコードされている

@app.route('/user')
def get_user():
    """ユーザー情報を取得する（つもりの）エンドポイント"""
    username = request.args.get('username')
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    # CWE-89: SQLインジェクション
    # 脆弱性: ユーザー入力を直接SQLクエリに埋め込んでいる
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    user_data = cursor.fetchone()
    db.close()
    return str(user_data)


@app.route('/ping')
def ping_host():
    """指定されたホストにpingを送信するエンドポイント"""
    host = request.args.get('host')

    # CWE-78: OSコマンドインジェクション
    # 脆弱性: ユーザー入力をサニタイズせずにOSコマンドとして実行している
    os.system(f"ping -c 1 {host}")

    return f"Pinged {host}"


@app.route('/file')
def read_file():
    """指定されたファイルの内容を表示するエンドポイント"""
    filename = request.args.get('filename')
    base_path = "/var/www/data/"

    # CWE-22: パストラバーサル
    # 脆弱性: ユーザー入力のパスを検証せずに結合している
    file_path = os.path.join(base_path, filename)

    with open(file_path, 'r') as f:
        content = f.read()

    return content

# --- メイン処理 ---
if __name__ == '__main__':
    # 注意: このコードはデバッグモードで実行されます。本番環境では絶対に使用しないでください。
    app.run(debug=True)