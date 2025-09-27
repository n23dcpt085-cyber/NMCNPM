import mysql.connector, hashlib
from decimal import Decimal

DB_CONFIG = {
    "user": "root",
    "password": "101097",      # đổi theo MySQL của bạn
    "host": "localhost",
    "database": "lab07"
}

def verify_pin(card_no, pin):
    """Kiểm tra PIN nhập vào có khớp hash trong DB không"""
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return False
    return row[0] == hashlib.sha256(pin.encode()).hexdigest()

def withdraw(card_no, amount):
    """Thực hiện giao dịch rút tiền"""
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        conn.start_transaction()

        # Lấy số dư và khóa hàng FOR UPDATE
        cur.execute("""
            SELECT a.account_id, a.balance 
            FROM accounts a 
            JOIN cards c ON a.account_id=c.account_id 
            WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        row = cur.fetchone()
        if not row:
            raise Exception("Card not found")
        account_id, balance = row
        balance = Decimal(balance)
        if balance < amount:
            raise Exception("Insufficient funds")

        # Cập nhật số dư
        cur.execute(
            "UPDATE accounts SET balance=balance-%s WHERE account_id=%s",
            (amount, account_id)
        )

        # Ghi transaction log
        cur.execute("""
            INSERT INTO transactions(account_id,card_no,atm_id,tx_type,amount,balance_after)
            VALUES(%s,%s,1,'WITHDRAW',%s,%s)
        """, (account_id, card_no, amount, balance-amount))

        conn.commit()
        print(f"✅ Withdraw success. Rút {amount}. Số dư còn lại: {balance-amount}")
    except Exception as e:
        conn.rollback()
        print("❌ Error:", e)
    finally:
        conn.close()

# --- Demo chạy ---

"""
Cách chạy chương trình
python.exe .\withdraw_module.py
Nhập mã pin: 1234
Nhập số tiền theo formart: x.x
"""
if __name__ == "__main__":
    card = "1111222233334444"
    pin = input("Nhập PIN: ")
    if verify_pin(card, pin):
        try:
            amt_str = input("Nhập số tiền muốn rút: ")
            amt = Decimal(amt_str)
            withdraw(card, amt)
        except ValueError:
            print("Số tiền không hợp lệ.")
    else:
        print("Sai PIN hoặc thẻ không tồn tại.")
