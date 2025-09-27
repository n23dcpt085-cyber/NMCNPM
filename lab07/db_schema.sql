CREATE DATABASE IF NOT EXISTS atm_demo;
USE atm_demo;

-- Bảng accounts
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    owner_name VARCHAR(100),
    balance DECIMAL(15,2) DEFAULT 0
);

-- Bảng cards
CREATE TABLE cards (
    card_no VARCHAR(20) PRIMARY KEY,
    account_id INT,
    pin_hash CHAR(64),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Bảng transactions
CREATE TABLE transactions (
    tx_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    card_no VARCHAR(20),
    atm_id INT,
    tx_type VARCHAR(20),
    amount DECIMAL(15,2),
    balance_after DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
