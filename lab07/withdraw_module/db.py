# db.py
import mysql.connector
from withdraw_module.config import DB_CONFIG

def get_connection():
    """Tạo kết nối tới database"""
    return mysql.connector.connect(**DB_CONFIG)
