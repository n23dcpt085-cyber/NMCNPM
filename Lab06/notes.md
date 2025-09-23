# Lab06 – Thiết kế chi tiết lớp & kiến trúc ATM

## 1. Class Diagram
- Gồm các lớp chính: `ATM`, `Card`, `Account`, `Transaction`.
- Các quan hệ:
  - `ATM` quản lý `Card` và tạo `Transaction`.
  - `Card` liên kết với `Account`.
  - `Account` tham gia vào `Transaction`.

## 2. Package Diagram
- **UI**: Form giao diện cho người dùng (LoginForm, TransactionForm).
- **Controller**: Trung gian giữa UI và Services (ATMController).
- **BankService**: Xử lý nghiệp vụ (AccountService, TransactionService).
- **Hardware**: Thiết bị phần cứng (CardReader, CashDispenser, Printer).

## 3. Ghi chú
- UML được vẽ bằng PlantUML.
- Xuất file `.png` từ `.puml` để demo.
- Đảm bảo đầy đủ artifacts trong thư mục `/labs/lab06-atm-class/`.

