USE atm_demo;

-- Thêm dữ liệu demo để test Withdraw Module

-- 1. Tài khoản có sẵn số dư 10,000,000
INSERT INTO accounts (owner_name, balance)
VALUES ('Nguyen Van A', 10000000);

-- 2. Thẻ ATM liên kết với tài khoản trên
-- Card number: 1234567890
-- PIN: 1234 (hash SHA256)
INSERT INTO cards (card_no, account_id, pin_hash)
VALUES (
    '1234567890',
    1,
    SHA2('1234', 256)
);
