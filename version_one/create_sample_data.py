#!/usr/bin/env python
"""
Script tạo dữ liệu mẫu cho website Tuệ Linh Land
Usage: python create_sample_data.py
"""

import os
import sys
import django
from datetime import datetime, timedelta
from decimal import Decimal
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuelinh_real_estate.settings')
sys.path.append('/home/worker/tuelinh_release/official_version')
django.setup()

from django.contrib.auth.models import User
from properties.models import PropertyType, Property
from news.models import Category, News, NewsTag, NewsTagRelation
from contacts.models import Contact, Newsletter

def create_superuser():
    """Tạo superuser nếu chưa có"""
    print("🔐 Tạo superuser...")
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@tuelinh.com',
            password='admin123',
            first_name='Admin',
            last_name='Tuệ Linh'
        )
        print("   ✅ Đã tạo superuser: admin/admin123")
    else:
        print("   ℹ️  Superuser đã tồn tại")

def create_property_types():
    """Tạo loại hình bất động sản"""
    print("🏠 Tạo loại hình bất động sản...")
    
    property_types = [
        {'name': 'Căn hộ chung cư', 'slug': 'can-ho-chung-cu'},
        {'name': 'Nhà riêng', 'slug': 'nha-rieng'},
        {'name': 'Biệt thự', 'slug': 'biet-thu'},
        {'name': 'Shophouse', 'slug': 'shophouse'},
        {'name': 'Đất nền', 'slug': 'dat-nen'},
        {'name': 'Kho xưởng', 'slug': 'kho-xuong'},
        {'name': 'Văn phòng', 'slug': 'van-phong'},
        {'name': 'Mặt bằng kinh doanh', 'slug': 'mat-bang-kinh-doanh'}
    ]
    
    created_count = 0
    for pt_data in property_types:
        property_type, created = PropertyType.objects.get_or_create(
            slug=pt_data['slug'],
            defaults={'name': pt_data['name']}
        )
        if created:
            created_count += 1
    
    print(f"   ✅ Đã tạo {created_count} loại hình bất động sản mới")
    return PropertyType.objects.all()

def create_properties(property_types):
    """Tạo dữ liệu bất động sản mẫu"""
    print("🏡 Tạo dữ liệu bất động sản...")
    
    locations = [
        'Quận 1, TP.HCM', 'Quận 2, TP.HCM', 'Quận 3, TP.HCM', 'Quận 7, TP.HCM',
        'Quận Bình Thạnh, TP.HCM', 'Quận Tân Bình, TP.HCM', 'Hà Nội', 'Đà Nẵng',
        'Biên Hòa, Đồng Nai', 'Thủ Dầu Một, Bình Dương', 'Nha Trang', 'Vũng Tàu'
    ]
    
    descriptions = [
        "Căn hộ cao cấp với view đẹp, nội thất sang trọng, tiện ích đầy đủ.",
        "Nhà mới xây, thiết kế hiện đại, gần trường học và bệnh viện.",
        "Biệt thự sang trọng trong khu compound an ninh, có hồ bơi riêng.",
        "Shophouse mặt tiền đường lớn, vị trí kinh doanh tuyệt vời.",
        "Đất nền sổ đỏ trao tay, pháp lý rõ ràng, giá đầu tư hấp dẫn.",
        "Văn phòng hạng A tại trung tâm thành phố, view panorama.",
        "Kho xưởng hiện đại, diện tích lớn, giao thông thuận tiện.",
        "Mặt bằng kinh doanh sầm uất, foot traffic cao, doanh thu ổn định."
    ]
    
    sample_properties = []
    created_count = 0
    
    for i in range(50):  # Tạo 50 bất động sản mẫu
        property_type = random.choice(property_types)
        location = random.choice(locations)
        
        # Tạo giá dựa trên loại hình
        if 'chung-cu' in property_type.slug:
            price_range = (2, 15)  # 2-8 tỷ
            area_range = (50, 150)
            bedrooms_range = (1, 4)
            bathrooms_range = (1, 3)
        elif 'biet-thu' in property_type.slug:
            price_range = (8, 35)  # 8-25 tỷ
            area_range = (200, 500)
            bedrooms_range = (3, 6)
            bathrooms_range = (3, 5)
        elif 'dat-nen' in property_type.slug:
            price_range = (1, 5)  # 1-5 tỷ
            area_range = (80, 300)
            bedrooms_range = (0, 0)
            bathrooms_range = (0, 0)
        else:
            price_range = (1, 15)  # 1.5-12 tỷ
            area_range = (60, 250)
            bedrooms_range = (1, 5)
            bathrooms_range = (1, 4)
        
        price = random.randint(*price_range)
        area = random.uniform(*area_range)
        bedrooms = random.randint(*bedrooms_range)
        bathrooms = random.randint(*bathrooms_range)
        
        # Tạo status ngẫu nhiên
        status = random.choice(['available', 'sold', 'reserved'])
        
        property_data = {
            'title': f"{property_type.name} {area:.0f}m² tại {location}",
            'description': random.choice(descriptions) + f" Diện tích {area:.0f}m², {bedrooms} phòng ngủ, {bathrooms} phòng tắm." if bedrooms > 0 else random.choice(descriptions) + f" Diện tích {area:.0f}m².",
            'property_type': property_type,
            'price': Decimal(str(price)),
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'address': f"Địa chỉ cụ thể tại {location}",
            'city': location.split(', ')[-1] if ', ' in location else location,
            'district': location.split(', ')[0] if ', ' in location else '',
            'ward': f"Phường {random.randint(1, 15)}",
            'status': status,
            'featured': random.choice([True, False]),
            'created_at': datetime.now() - timedelta(days=random.randint(1, 365))
        }
        
        property_obj, created = Property.objects.get_or_create(
            title=property_data['title'],
            defaults=property_data
        )
        
        if created:
            created_count += 1
            sample_properties.append(property_obj)
    
    print(f"   ✅ Đã tạo {created_count} bất động sản mới")
    return sample_properties

def create_news_categories():
    """Tạo danh mục tin tức"""
    print("📂 Tạo danh mục tin tức...")
    
    categories = [
        {'name': 'Tin thị trường', 'slug': 'tin-thi-truong', 'description': 'Thông tin, phân tích thị trường bất động sản'},
        {'name': 'Dự án mới', 'slug': 'du-an-moi', 'description': 'Giới thiệu các dự án bất động sản mới'},
        {'name': 'Phong thủy', 'slug': 'phong-thuy', 'description': 'Kiến thức phong thủy trong bất động sản'},
        {'name': 'Tư vấn đầu tư', 'slug': 'tu-van-dau-tu', 'description': 'Hướng dẫn đầu tư bất động sản hiệu quả'},
        {'name': 'Pháp lý', 'slug': 'phap-ly', 'description': 'Kiến thức pháp lý về bất động sản'},
        {'name': 'Tin công ty', 'slug': 'tin-cong-ty', 'description': 'Tin tức về công ty Tuệ Linh Land'}
    ]
    
    created_count = 0
    created_categories = []
    
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name'], 'description': cat_data['description']}
        )
        if created:
            created_count += 1
        created_categories.append(category)
    
    print(f"   ✅ Đã tạo {created_count} danh mục tin tức mới")
    return created_categories

def create_news_tags():
    """Tạo tags cho tin tức"""
    print("🏷️  Tạo tags tin tức...")
    
    tags = [
        'Căn hộ', 'Biệt thự', 'Đất nền', 'Shophouse', 'Đầu tư', 'Cho thuê',
        'TP.HCM', 'Hà Nội', 'Đà Nẵng', 'Bình Dương', 'Đồng Nai',
        'Phong thủy', 'Pháp lý', 'Thị trường', 'Giá cả', 'Xu hướng',
        'Mua bán', 'Tư vấn', 'Hướng dẫn', 'Kinh nghiệm', 'Mẹo hay'
    ]
    
    created_count = 0
    created_tags = []
    
    for tag_name in tags:
        tag, created = NewsTag.objects.get_or_create(
            name=tag_name,
            defaults={'slug': tag_name.lower().replace(' ', '-')}
        )
        if created:
            created_count += 1
        created_tags.append(tag)
    
    print(f"   ✅ Đã tạo {created_count} tags mới")
    return created_tags

def create_news_articles(categories, tags):
    """Tạo bài viết tin tức mẫu"""
    print("📰 Tạo bài viết tin tức...")
    
    # Tạo user author nếu chưa có
    author, created = User.objects.get_or_create(
        username='author',
        defaults={
            'email': 'author@tuelinh.com',
            'first_name': 'Biên tập',
            'last_name': 'Viên',
            'is_staff': True
        }
    )
    if created:
        author.set_password('author123')
        author.save()
    
    news_data = [
        {
            'title': 'Thị trường bất động sản cuối năm 2024: Xu hướng và dự báo',
            'excerpt': 'Phân tích tổng quan về thị trường bất động sản Việt Nam cuối năm 2024 và dự báo cho năm 2025.',
            'content': '''<p>Thị trường bất động sản Việt Nam cuối năm 2024 đang cho thấy những dấu hiệu phục hồi tích cực sau giai đoạn khó khăn. Theo các chuyên gia, nguồn cung căn hộ tại TP.HCM và Hà Nội đang dần ổn định.</p>

<h3>Những điểm nổi bật của thị trường</h3>
<ul>
<li>Giá bán có xu hướng ổn định, không tăng đột biến như những năm trước</li>
<li>Nguồn cung mới tập trung ở phân khúc trung cấp và cao cấp</li>
<li>Các dự án có pháp lý rõ ràng được ưa chuộng</li>
<li>Khu vực ngoại thành phát triển mạnh</li>
</ul>

<h3>Dự báo cho năm 2025</h3>
<p>Năm 2025 được dự báo sẽ là năm bứt phá của thị trường bất động sản với nhiều chính sách hỗ trợ từ Chính phủ và nhu cầu thực tế gia tăng.</p>''',
            'category': 'tin-thi-truong',
            'tags': ['Thị trường', 'Xu hướng', 'TP.HCM', 'Hà Nội']
        },
        {
            'title': 'Top 5 dự án căn hộ đáng chú ý tại TP.HCM năm 2024',
            'excerpt': 'Điểm qua 5 dự án căn hộ chung cư được quan tâm nhất tại TP.HCM trong năm 2024.',
            'content': '''<p>TP.HCM tiếp tục khẳng định vị thế là trung tâm kinh tế lớn nhất cả nước với nhiều dự án căn hộ chất lượng cao được ra mắt.</p>

<h3>1. Dự án A - Quận 7</h3>
<p>Vị trí đắc địa, view sông, tiện ích đầy đủ. Giá từ 45 triệu/m².</p>

<h3>2. Dự án B - Quận 2</h3>
<p>Căn hộ thông minh, công nghệ hiện đại. Giá từ 50 triệu/m².</p>

<h3>3. Dự án C - Bình Thạnh</h3>
<p>Kết nối giao thông thuận tiện, gần trung tâm. Giá từ 40 triệu/m².</p>

<h3>4. Dự án D - Tân Bình</h3>
<p>Phù hợp đầu tư cho thuê, rental yield cao. Giá từ 38 triệu/m².</p>

<h3>5. Dự án E - Quận 9</h3>
<p>Giá hợp lý, tiềm năng tăng giá trong tương lai. Giá từ 35 triệu/m².</p>''',
            'category': 'du-an-moi',
            'tags': ['Căn hộ', 'TP.HCM', 'Dự án mới', 'Đầu tư']
        },
        {
            'title': 'Phong thủy khi chọn mua căn hộ: 7 điều cần lưu ý',
            'excerpt': 'Hướng dẫn chi tiết về phong thủy khi chọn mua căn hộ để mang lại may mắn và thịnh vượng.',
            'content': '''<p>Phong thủy đóng vai trò quan trọng trong việc chọn lựa nơi ở. Dưới đây là 7 điều cần lưu ý về phong thủy khi mua căn hộ.</p>

<h3>1. Hướng căn hộ</h3>
<p>Chọn hướng phù hợp với mệnh của gia chủ. Hướng Đông và Đông Nam thường được ưa chuộng.</p>

<h3>2. Vị trí tầng</h3>
<p>Tránh tầng 4, 14, 24... theo quan niệm phong thủy. Tầng 8, 18, 28... được coi là may mắn.</p>

<h3>3. Hình dạng căn hộ</h3>
<p>Ưu tiên căn hộ có hình chữ nhật hoặc vuông vắn, tránh hình tam giác hoặc bất quy tắc.</p>

<h3>4. Cửa chính</h3>
<p>Cửa chính không nên đối diện thang máy, thang bộ hoặc toilet.</p>

<h3>5. Bếp và toilet</h3>
<p>Bếp và toilet không nên nằm ở trung tâm căn hộ.</p>

<h3>6. Ánh sáng tự nhiên</h3>
<p>Căn hộ cần có đủ ánh sáng tự nhiên, thoáng khí.</p>

<h3>7. Môi trường xung quanh</h3>
<p>Tránh căn hộ gần nghĩa trang, bệnh viện hoặc những nơi có khí xấu.</p>''',
            'category': 'phong-thuy',
            'tags': ['Phong thủy', 'Căn hộ', 'Mua bán', 'Tư vấn']
        },
        {
            'title': 'Hướng dẫn đầu tư bất động sản cho người mới bắt đầu',
            'excerpt': 'Kinh nghiệm và bí quyết đầu tư bất động sản hiệu quả dành cho người mới bắt đầu.',
            'content': '''<p>Đầu tư bất động sản là kênh đầu tư phổ biến và hiệu quả. Dưới đây là hướng dẫn chi tiết cho người mới bắt đầu.</p>

<h3>Bước 1: Xác định mục tiêu đầu tư</h3>
<ul>
<li>Đầu tư để ở: Ưu tiên vị trí, tiện ích</li>
<li>Đầu tư cho thuê: Tính toán rental yield</li>
<li>Đầu tư chờ tăng giá: Nghiên cứu quy hoạch</li>
</ul>

<h3>Bước 2: Chuẩn bị tài chính</h3>
<p>Thường cần 30-50% giá trị bất động sản làm vốn ban đầu. Phần còn lại có thể vay ngân hàng.</p>

<h3>Bước 3: Nghiên cứu thị trường</h3>
<ul>
<li>Tìm hiểu giá cả khu vực</li>
<li>Kiểm tra quy hoạch phát triển</li>
<li>Đánh giá tiềm năng tăng trưởng</li>
</ul>

<h3>Bước 4: Chọn vị trí đầu tư</h3>
<p>3 yếu tố quan trọng: Vị trí - Vị trí - Vị trí. Ưu tiên gần trung tâm, giao thông thuận tiện.</p>

<h3>Bước 5: Thẩm định pháp lý</h3>
<p>Kiểm tra kỹ các giấy tờ: sổ đỏ, giấy phép xây dựng, giấy phép kinh doanh...</p>''',
            'category': 'tu-van-dau-tu',
            'tags': ['Đầu tư', 'Hướng dẫn', 'Kinh nghiệm', 'Mẹo hay']
        },
        {
            'title': 'Quy trình mua bán bất động sản và những lưu ý pháp lý',
            'excerpt': 'Hướng dẫn chi tiết quy trình mua bán bất động sản và những điều cần lưu ý về mặt pháp lý.',
            'content': '''<p>Mua bán bất động sản là giao dịch lớn trong đời, cần thực hiện đúng quy trình và lưu ý các vấn đề pháp lý.</p>

<h3>Quy trình mua bán</h3>

<h4>1. Giai đoạn tìm hiểu</h4>
<ul>
<li>Xác định nhu cầu và ngân sách</li>
<li>Tìm kiếm thông tin bất động sản</li>
<li>Khảo sát thực tế</li>
</ul>

<h4>2. Giai đoạn đàm phán</h4>
<ul>
<li>Thỏa thuận giá cả</li>
<li>Ký hợp đồng đặt cọc</li>
<li>Thẩm định pháp lý</li>
</ul>

<h4>3. Giai đoạn hoàn tất</h4>
<ul>
<li>Ký hợp đồng chính thức</li>
<li>Thanh toán</li>
<li>Làm thủ tục chuyển nhượng</li>
</ul>

<h3>Những lưu ý pháp lý quan trọng</h3>

<h4>Kiểm tra giấy tờ</h4>
<ul>
<li>Sổ đỏ/Sổ hồng gốc</li>
<li>Chứng minh nhân dân của chủ sở hữu</li>
<li>Giấy tờ chứng minh nguồn gốc</li>
</ul>

<h4>Thẩm định pháp lý</h4>
<ul>
<li>Kiểm tra tại Sở Tài nguyên Môi trường</li>
<li>Xác minh thông tin chủ sở hữu</li>
<li>Kiểm tra các khoản nợ, thế chấp</li>
</ul>''',
            'category': 'phap-ly',
            'tags': ['Pháp lý', 'Mua bán', 'Hướng dẫn', 'Quy trình']
        }
    ]
    
    created_count = 0
    created_articles = []
    
    for article_data in news_data:
        # Tìm category
        category = next((c for c in categories if c.slug == article_data['category']), categories[0])
        
        news_article, created = News.objects.get_or_create(
            title=article_data['title'],
            defaults={
                'slug': article_data['title'].lower().replace(' ', '-').replace(':', '').replace(',', ''),
                'excerpt': article_data['excerpt'],
                'content': article_data['content'],
                'category': category,
                'author': author,
                'status': 'published',
                'created_at': datetime.now() - timedelta(days=random.randint(1, 30)),
                'published_at': datetime.now() - timedelta(days=random.randint(1, 30))
            }
        )
        
        if created:
            created_count += 1
            created_articles.append(news_article)
            
            # Thêm tags
            article_tags = [tag for tag in tags if tag.name in article_data['tags']]
            for tag in article_tags:
                NewsTagRelation.objects.get_or_create(
                    news=news_article,
                    tag=tag
                )
    
    print(f"   ✅ Đã tạo {created_count} bài viết tin tức mới")
    return created_articles

def create_sample_contacts():
    """Tạo dữ liệu liên hệ mẫu"""
    print("📞 Tạo dữ liệu liên hệ mẫu...")
    
    sample_contacts = [
        {
            'name': 'Nguyễn Văn A',
            'email': 'nguyenvana@email.com',
            'phone': '0901234567',
            'message': 'Tôi muốn tìm hiểu về căn hộ 2PN tại Quận 7, giá khoảng 3-4 tỷ.'
        },
        {
            'name': 'Trần Thị B',
            'email': 'tranthib@email.com',
            'phone': '0912345678',
            'message': 'Cần tư vấn đầu tư đất nền tại Bình Dương, vốn khoảng 2 tỷ.'
        },
        {
            'name': 'Lê Văn C',
            'email': 'levanc@email.com',
            'phone': '0923456789',
            'message': 'Muốn bán căn hộ chung cư tại Quận 2, diện tích 80m2.'
        },
        {
            'name': 'Phạm Thị D',
            'email': 'phamthid@email.com',
            'phone': '0934567890',
            'message': 'Tìm shophouse cho thuê tại Quận 1, mặt tiền rộng.'
        },
        {
            'name': 'Hoàng Văn E',
            'email': 'hoangvane@email.com',
            'phone': '0945678901',
            'message': 'Cần tư vấn pháp lý về việc chuyển nhượng bất động sản.'
        }
    ]
    
    created_count = 0
    for contact_data in sample_contacts:
        contact, created = Contact.objects.get_or_create(
            email=contact_data['email'],
            defaults=contact_data
        )
        if created:
            created_count += 1
    
    print(f"   ✅ Đã tạo {created_count} liên hệ mẫu")

def create_newsletter_subscriptions():
    """Tạo đăng ký newsletter mẫu"""
    print("📧 Tạo đăng ký newsletter mẫu...")
    
    emails = [
        'customer1@email.com', 'customer2@email.com', 'customer3@email.com',
        'investor1@email.com', 'investor2@email.com', 'buyer1@email.com',
        'seller1@email.com', 'agent1@email.com', 'client1@email.com',
        'prospect1@email.com'
    ]
    
    created_count = 0
    for email in emails:
        newsletter, created = Newsletter.objects.get_or_create(
            email=email,
            defaults={'subscribed_at': datetime.now() - timedelta(days=random.randint(1, 100))}
        )
        if created:
            created_count += 1
    
    print(f"   ✅ Đã tạo {created_count} đăng ký newsletter mới")

def main():
    """Hàm chính"""
    print("🚀 BẮT ĐẦU TẠO DỮ LIỆU MẪU CHO WEBSITE TUỆ LINH LAND")
    print("=" * 60)
    
    try:
        # 1. Tạo superuser
        create_superuser()
        
        # 2. Tạo loại hình bất động sản
        property_types = create_property_types()
        
        # 3. Tạo bất động sản mẫu
        properties = create_properties(property_types)
        
        # 4. Tạo danh mục tin tức
        categories = create_news_categories()
        
        # 5. Tạo tags tin tức
        tags = create_news_tags()
        
        # 6. Tạo bài viết tin tức
        articles = create_news_articles(categories, tags)
        
        # 7. Tạo liên hệ mẫu
        create_sample_contacts()
        
        # 8. Tạo đăng ký newsletter
        create_newsletter_subscriptions()
        
        print("\n" + "=" * 60)
        print("🎉 HOÀN THÀNH TẠO DỮ LIỆU MẪU!")
        print("=" * 60)
        print(f"📊 Tổng kết:")
        print(f"   🏠 Bất động sản: {Property.objects.count()}")
        print(f"   📰 Tin tức: {News.objects.count()}")
        print(f"   📂 Danh mục: {Category.objects.count()}")
        print(f"   🏷️  Tags: {NewsTag.objects.count()}")
        print(f"   📞 Liên hệ: {Contact.objects.count()}")
        print(f"   📧 Newsletter: {Newsletter.objects.count()}")
        print(f"\n🔐 Tài khoản admin: admin/admin123")
        print(f"🔐 Tài khoản author: author/author123")
        print(f"🌐 Truy cập: http://127.0.0.1:8000/admin")
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
