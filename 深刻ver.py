import sqlite3

def insecure_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # CWE-89: SQLインジェクション（ユーザ入力の直接埋め込み）
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None

def main():
    print("=== 脆弱なログインシステム ===")
    username = input("ユーザー名: ")
    password = input("パスワード: ")
    if insecure_login(username, password):
        print("ログイン成功")
    else:
        print("ログイン失敗")

if __name__ == "__main__":
    main()
