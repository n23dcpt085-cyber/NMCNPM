# Use Case
1. Use Case: Đặt phòng
    Tên: Đặt phòng
    Tác nhân: Khách hàng
    Mục tiêu: Giúp khách hàng chọn và giữ chỗ phòng khách sạn.
    Điều kiện tiên quyết: Khách hàng đã đăng nhập.
    Kịch bản chính:
    Khách hàng tìm kiếm phòng trống.
    Hệ thống hiển thị danh sách phòng còn trống.
    Khách hàng chọn phòng muốn đặt.
    Hệ thống lưu thông tin đặt phòng.
    Hệ thống yêu cầu khách hàng thanh toán.
    Kết quả: Phòng được đặt thành công.
    Ngoại lệ:
    Nếu phòng đã có người đặt → thông báo lỗi.
    Nếu khách hàng hủy giữa chừng → thoát giao dịch.

2. Use Case: Thanh toán
    Tên: Thanh toán
    Tác nhân: Khách hàng, Hệ thống thanh toán
    Mục tiêu: Xử lý thanh toán cho đặt phòng.
    Điều kiện tiên quyết: Khách hàng đã chọn phòng để đặt.
    Kịch bản chính:
    Hệ thống yêu cầu khách hàng chọn phương thức thanh toán (thẻ, ví điện tử,...).
    Khách hàng nhập thông tin thanh toán.
    Hệ thống gửi yêu cầu đến hệ thống thanh toán.
    Hệ thống thanh toán xác nhận giao dịch.
    Hệ thống lưu lại kết quả và thông báo cho khách hàng.
    Kết quả: Thanh toán thành công, đặt phòng hoàn tất.
    Ngoại lệ:
    Thông tin thẻ sai → báo lỗi.
    Không đủ tiền → từ chối thanh toán.