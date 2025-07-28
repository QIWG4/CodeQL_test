import os

def main():
    print("=== 電卓ツール（Python）===")
    print("1. 四則演算")
    print("2. コマンド実行")
    print("3. ファイル読み込み")
    choice = input("選択してください: ")

    if choice == "1":
        expr = input("計算式を入力してください (例: 1+2): ")
        print("結果:", eval(expr))  # CWE-94
    elif choice == "2":
        cmd = input("実行するコマンドを入力してください: ")
        os.system(cmd)  # CWE-78
    elif choice == "3":
        filename = input("ファイルパスを入力してください: ")
        with open(filename, 'r') as f:  # CWE-22
            print(f.read())
    else:
        print("無効な選択です。")

if __name__ == "__main__":
    main()
