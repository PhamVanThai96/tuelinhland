# Tuệ Linh Real Estate Website

This is the website for Tuệ Linh Real Estate, a leading real estate company in Vietnam.

## Khởi tạo dự án từ đầu

1. **Cài đặt Python (nếu chưa có):**
   ```bash
   # Kiểm tra phiên bản Python
   python3 --version
   
   # Cài đặt Python nếu cần
   # Ubuntu/Debian
   # sudo apt update
   # sudo apt install python3 python3-pip python3-venv
   
   # CentOS/RHEL
   # sudo yum install python3 python3-pip
   ```

2. **Tạo thư mục dự án và cd vào:**
   ```bash
   mkdir tuelinh
   cd tuelinh
   ```

3. **Tạo và kích hoạt môi trường ảo:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Trên Linux/macOS
   # venv\Scripts\activate  # Trên Windows
   ```

4. **Cài đặt Django:**
   ```bash
   pip install django pillow django-ckeditor
   pip freeze > requirements.txt
   ```

5. **Khởi tạo dự án Django:**
   ```bash
   django-admin startproject tuelinh_real_estate .
   ```

6. **Tạo các ứng dụng cần thiết:**
   ```bash
   python manage.py startapp frontend
   python manage.py startapp property
   python manage.py startapp blog
   python manage.py startapp accounts
   ```

7. **Cập nhật cài đặt trong settings.py:**
   ```bash
   # Mở file settings.py và thêm các ứng dụng vào INSTALLED_APPS
   # Cấu hình cơ sở dữ liệu
   # Cấu hình ngôn ngữ và múi giờ
   ```

8. **Tạo cấu trúc thư mục cho templates và static files:**
   ```bash
   mkdir -p frontend/templates/frontend
   mkdir -p frontend/static/frontend/{css,js,images}
   touch frontend/templates/frontend/base.html
   touch frontend/templates/frontend/home.html
   ```

9. **Tạo model cơ bản:**
   ```bash
   # Chỉnh sửa file models.py trong các app tương ứng
   ```

10. **Tạo migrations và áp dụng:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

11. **Tạo superuser để quản lý admin:**
    ```bash
    python manage.py createsuperuser
    ```

12. **Thu thập static files:**
    ```bash
    python manage.py collectstatic
    ```

13. **Chạy máy chủ phát triển:**
    ```bash
    python manage.py runserver
    ```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd tuelinh
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**
    *   Set up your database (e.g., PostgreSQL, MySQL).
    *   Update the `DATABASES` settings in `tuelinh_real_estate/settings.py` with your database credentials.

5.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Collect static files:**
    ```bash
    python manage.py collectstatic
    ```

8.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1.  **Homepage:** Visit the homepage at `http://127.0.0.1:8000/` to see featured properties and company information.
2.  **Property Listings:** Browse available properties by type (apartment, house, villa) using the "DỰ ÁN" dropdown menu.
3.  **Admin Interface:** Access the admin interface at `http://127.0.0.1:8000/admin/` to manage data (requires a superuser).
4.  **Contact:** Contact us through the "BÀI VIẾT" link in the navigation bar.
5.  **Newsletter:** Subscribe to our newsletter in the footer to receive updates on new properties and promotions.

## Development

### Project Structure Check
Before running the website, ensure you have these key files:
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies
- `tuelinh_real_estate/settings.py` - Django settings
- `tuelinh_real_estate/urls.py` - URL configuration

### Running the Website
1. **Check Python version:**
   ```bash
   python --version
   # Should be Python 3.8 or higher
   ```

2. **Verify Django installation:**
   ```bash
   python -c "import django; print(django.get_version())"
   ```

3. **Check project structure:**
   ```bash
   ls -la
   # Should show manage.py and project directories
   ```

4. **Test database connection:**
   ```bash
   python manage.py check
   ```

5. **Run development server with debug:**
   ```bash
   python manage.py runserver --settings=tuelinh_real_estate.settings
   ```

### Troubleshooting
- **ModuleNotFoundError:** Check if virtual environment is activated and dependencies are installed
- **Database errors:** Verify database configuration in settings.py
- **Static files not loading:** Run `python manage.py collectstatic`
- **Permission errors:** Check file permissions and virtual environment activation

### Quick Start Commands
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```
