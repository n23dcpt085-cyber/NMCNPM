# NMCNPM/lab08_testing/test_withdraw.py
import sys, os
import pytest
from unittest.mock import patch, MagicMock

# Đảm bảo Python hiểu NMCNPM là package root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from NMCNPM.lab07.withdraw_module.withdraw import withdraw


# ---- UNIT TEST CHO withdraw ----
@patch('NMCNPM.lab07.withdraw_module.withdraw.get_connection')
def test_withdraw_success(mock_get_connection):
    # Mock database connection và cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Mock fetchone trả về account info
    mock_cursor.fetchone.return_value = (1, 5000000)  # account_id=1, balance=5000000
    
    # Test rút tiền thành công
    withdraw("1234567890", 1000000)
    
    # Verify các method được gọi
    mock_conn.start_transaction.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()


@patch('NMCNPM.lab07.withdraw_module.withdraw.get_connection')
def test_withdraw_insufficient_funds(mock_get_connection):
    # Mock database connection và cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Mock fetchone trả về balance thấp
    mock_cursor.fetchone.return_value = (1, 500000)  # account_id=1, balance=500000
    
    # Test rút tiền với số dư không đủ
    withdraw("1234567890", 1000000)
    
    # Verify rollback được gọi
    mock_conn.rollback.assert_called_once()
    mock_conn.close.assert_called_once()


@patch('NMCNPM.lab07.withdraw_module.withdraw.get_connection')
def test_withdraw_card_not_found(mock_get_connection):
    # Mock database connection và cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Mock fetchone trả về None (không tìm thấy thẻ)
    mock_cursor.fetchone.return_value = None
    
    # Test với thẻ không tồn tại
    withdraw("9999999999", 1000000)
    
    # Verify rollback được gọi
    mock_conn.rollback.assert_called_once()
    mock_conn.close.assert_called_once()


# ---- UNIT TEST CHO verify_pin (nếu bạn muốn test hàm này) ----
# Trước tiên cần thêm hàm verify_pin vào withdraw.py

@patch('NMCNPM.lab07.withdraw_module.withdraw.get_connection')
def test_verify_pin_correct(mock_get_connection):
    # Chỉ chạy test này nếu đã thêm hàm verify_pin vào withdraw.py
    pass

@patch('NMCNPM.lab07.withdraw_module.withdraw.get_connection')  
def test_verify_pin_incorrect(mock_get_connection):
    # Chỉ chạy test này nếu đã thêm hàm verify_pin vào withdraw.py
    pass