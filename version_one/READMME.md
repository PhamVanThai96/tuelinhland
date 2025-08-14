# 🏠 TueLinh Land Real Estate Website

Website bất động sản chuyên nghiệp được xây dựng bằng Django với giao diện hiện đại và tính năng đa dạng.

## 📦 Cài đặt

### 1. Tạo virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate     # Windows
```

### 2. Cài đặt dependencies
```bash
# Cài đặt tự động tất cả thư viện
./install_ui_libs.sh

# Hoặc cài đặt thủ công
pip install -r requirements.txt
```

### 3. Thiết lập môi trường
```bash
# Copy file cấu hình mẫu
cp .env.example .env
# Chỉnh sửa .env theo môi trường của bạn
```

### 4. Thiết lập database
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### 5. Chạy server
```bash
# Development
python manage.py runserver

# Production
./deploy.sh
```

## 🎨 Thư viện UI được sử dụng

### Form & Styling
- **Django Crispy Forms + Bootstrap 5**: Form styling đẹp mắt
- **Django Widget Tweaks**: Tùy chỉnh form widgets
- **Django Bootstrap 5**: Tích hợp Bootstrap

### Media & Content
- **Easy Thumbnails**: Tối ưu hóa hình ảnh
- **Django CKEditor**: Rich text editor
- **Django Summernote**: Alternative rich editor

### Enhanced Widgets
- **Django Select2**: Dropdown nâng cao
- **Django Autocomplete Light**: Tìm kiếm tự động
- **Django ColorField**: Color picker

### Data Display
- **Django Tables2**: Bảng dữ liệu đẹp
- **Django ChartJS**: Biểu đồ tương tác

### User Experience
- **Django Notifications**: Hệ thống thông báo
- **Django Activity Stream**: Theo dõi hoạt động
- **Django Taggit**: Hệ thống tag

### Admin Interface
- **Django Admin Interface**: Giao diện admin đẹp
- **Django Grappelli**: Theme admin chuyên nghiệp

## 🛠️ Development Tools

- **Django Debug Toolbar**: Debug & profiling
- **Django Extensions**: Các tiện ích phát triển
- **Django Browser Reload**: Live reload
- **Pytest**: Testing framework
- **Black, Flake8, isort**: Code formatting

## 📱 Tính năng chính

- ✅ Responsive design với Bootstrap 5
- ✅ Quản lý bất động sản
- ✅ Hệ thống liên hệ
- ✅ Tin tức và blog
- ✅ Admin interface hiện đại
- ✅ SEO optimization
- ✅ Image optimization
- ✅ Rich text editing

## 🚀 Production Deployment

```bash
# Chạy script deploy tự động
./deploy.sh

# Hoặc thủ công:
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn tuelinh_real_estate.wsgi:application
```

## 📁 Cấu trúc dự án

```
tuelinh_release/official_version/
├── manage.py
├── requirements.txt          # Tất cả dependencies
├── .env.example             # File cấu hình mẫu
├── install_ui_libs.sh       # Script cài đặt
├── deploy.sh                # Script deploy production
├── frontend/                # Main app
├── properties/              # Real estate properties
├── contacts/                # Contact management  
├── news/                    # News & blog
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
└── tuelinh_real_estate/     # Django settings
```

## 💡 Scripts có sẵn

### **install_ui_libs.sh** - Cài đặt development
```bash
./install_ui_libs.sh
```

### **deploy.sh** - Deploy production
```bash
./deploy.sh
```

## 💡 Tips

- Sử dụng `python manage.py shell_plus` để có enhanced shell
- Chạy `python manage.py show_urls` để xem tất cả URLs
- Sử dụng `python manage.py runserver_plus` cho development server nâng cao
- Show URL 'python manage.py show_urls'

python manage.py createcachetable || true

