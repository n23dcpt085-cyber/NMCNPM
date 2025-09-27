# withdraw.py
from withdraw_module.db import get_connection

def withdraw(card_no, amount):
    """Thực hiện rút tiền"""
    conn = get_connection()
    cur = conn.cursor()

    try:
        conn.start_transaction()

        # Khóa account để tránh race condition
        cur.execute("""
            SELECT account_id, balance 
            FROM accounts 
            JOIN cards USING(account_id) 
            WHERE card_no=%s FOR UPDATE
        """, (card_no,))
        row = cur.fetchone()

        if not row:
            raise Exception("Card not found")

        account_id, balance = row

        if balance < amount:
            raise Exception("Insufficient funds")

        # Update số dư
        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s",
                    (amount, account_id))

        # Log giao dịch
        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after) 
            VALUES (%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, balance - amount))

        conn.commit()
        print("Withdraw success. New balance:", balance - amount)

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        conn.close()
        
if __name__ == "__main__":
    card_no = "1234567890"
    amount = 2000000  # Rút 2 triệu
    withdraw(card_no, amount)
