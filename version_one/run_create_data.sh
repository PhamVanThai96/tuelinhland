#!/bin/bash
# Script chạy tạo sample data cho Django

echo "🚀 KHỞI TẠO DỮ LIỆU MẪU CHO WEBSITE TUỆ LINH LAND"
echo "================================================="

# Chuyển vào thư mục chính
cd /home/worker/tuelinh_release/official_version

# Kiểm tra môi trường
echo "🔍 Kiểm tra môi trường Django..."
python manage.py check --verbosity=0
if [ $? -ne 0 ]; then
    echo "❌ Lỗi cấu hình Django!"
    exit 1
fi

# Migrate database
echo "📊 Cập nhật database..."
python manage.py makemigrations --verbosity=0
python manage.py migrate --verbosity=0

# Chạy script tạo sample data
echo "📝 Tạo dữ liệu mẫu..."
cd /home/worker/tuelinh_release
python create_sample_data.py

echo ""
echo "✅ HOÀN THÀNH!"
echo "🌐 Khởi động server: cd official_version && python manage.py runserver"
echo "🔐 Admin: http://127.0.0.1:8000/admin (admin/admin123)"
