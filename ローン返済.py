import sqlite3
import math

DB_PATH = 'loans.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS loan_parameters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            principal REAL,
            annual_rate REAL,
            years INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def store_parameters(principal, annual_rate, years):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # 脆弱な SQL 結合
    query = f"INSERT INTO loan_parameters(principal, annual_rate, years) VALUES ({principal}, {annual_rate}, {years});"
    c.execute(query)
    conn.commit()
    conn.close()

def calculate_monthly_payment(principal, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    payment = principal * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return payment

if __name__ == "__main__":
    init_db()
    inp = input("ローン額（Principal）、年利％（Rate）、返済年数（Years）をカンマ区切りで入力してください: ")
    try:
        principal, annual_rate, years = inp.split(',')
        principal = float(principal)
        annual_rate = float(annual_rate)
        years = int(years)
    except:
        print("入力フォーマットが正しくありません。")
        exit(1)

    store_parameters(principal, annual_rate, years)
    payment = calculate_monthly_payment(principal, annual_rate, years)
    print(f"月々の返済額: {payment:.2f} 円")
