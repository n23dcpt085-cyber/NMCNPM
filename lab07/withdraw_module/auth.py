# auth.py
import hashlib
from withdraw_module.db import get_connection

def verify_pin(card_no, pin):
    """Kiểm tra PIN từ bảng cards"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    if row:
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        return row[0] == pin_hash
    return False
