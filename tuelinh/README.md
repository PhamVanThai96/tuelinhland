# Tuệ Linh Land - Hướng dẫn cài đặt & sử dụng

## 1. Yêu cầu hệ thống
- Python 3.8+
- pip
- virtualenv (khuyến nghị)
- SQLite (mặc định, không cần cài đặt thêm)

## 2. Cài đặt môi trường
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Cấu hình (nếu cần)
- Chỉnh sửa file `tuelinh/settings.py` để thay đổi thông tin cấu hình (nếu cần).
- Đảm bảo trường `SECRET_KEY` được bảo mật khi triển khai thực tế.

## 4. Khởi tạo database
```bash
python manage.py migrate
```

## 5. Tạo tài khoản quản trị
```bash
python manage.py createsuperuser
```

## 6. Chạy server phát triển
```bash
python manage.py runserver
```
Truy cập website tại: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 7. Quản trị nội dung
- Truy cập trang quản trị: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Đăng nhập bằng tài khoản quản trị vừa tạo.

## 8. Ghi chú
- Ảnh và file media sẽ được lưu trong thư mục `media/`.
- Nếu muốn upload ảnh, đảm bảo thư mục `media/` có quyền ghi.
- Để sử dụng Debug Toolbar, đảm bảo cài đặt đúng các package trong `requirements.txt`.

---
Mọi thắc mắc vui lòng liên hệ quản trị viên dự án.
