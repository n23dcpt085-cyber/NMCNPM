🛠️ Software Engineering Project – ATM Mini Project
📌 Giới thiệu

Dự án ATM Mini Project được phát triển trong môn Nhập môn Công nghệ Phần mềm.
Mục tiêu là áp dụng quy trình phát triển phần mềm, từ phân tích yêu cầu, thiết kế, lập trình, kiểm thử và triển khai, cụ thể:

Xây dựng hệ thống ATM mô phỏng.

Các chức năng: đăng nhập, rút tiền, quản lý tài khoản, lưu trữ lịch sử giao dịch.

Quản lý tiến độ dự án bằng Jira, lưu trữ code & artifacts trên GitHub.

👥 Thành viên nhóm

Nguyễn Văn A – Leader, Developer

Trần Thị B – Developer

Lê Văn C – Tester

Phạm Thị D – Documenter

🎯 Use Case chính

Quản lý người dùng (đăng nhập, đăng ký).

Quản lý tài khoản ATM (số dư, thông tin liên kết).

Xử lý giao dịch (rút tiền, nạp tiền).

Báo cáo & thống kê (lịch sử giao dịch).

(Use Case Diagram được lưu trong thư mục /artifacts/usecase-lab02.png)

📐 Thiết kế hệ thống

Use Case Diagram (Lab 02): mô tả chức năng chính.

Sequence Diagram (Lab 03): minh họa luồng rút tiền.

Class Diagram (Lab 06): mô hình các lớp chính: Account, ATM, Transaction.

ERD (Lab 05): mô hình cơ sở dữ liệu Users – Accounts – Transactions.

💻 Công nghệ sử dụng

Ngôn ngữ: Java (hoặc Python)

IDE: Visual Studio Code

CSDL: MySQL

Quản lý phiên bản: Git + GitHub

Mô hình phát triển: Agile – Scrum

🚀 Cài đặt & chạy thử

Clone repo:

git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>


Cài đặt database từ file db-script.sql, sau đó chạy chương trình:

Form login → nhập username/password từ DB.

Withdraw module → thực hiện giao dịch rút tiền.

📊 Quản lý & báo cáo

Test (Lab 08): đăng nhập đúng/sai, rút tiền hợp lệ/không hợp lệ.

Jira (Lab 09): quản lý backlog, sprint, burndown chart.

Lab 10: tích hợp toàn bộ artifacts, code và báo cáo.