#!/usr/bin/env python
"""
Script để fix slugs cho news có sẵn
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuelinh_real_estate.settings')
django.setup()

from news.models import News, vietnamese_slugify

def fix_news_slugs():
    """
    Fix all existing news slugs to be ASCII compatible
    """
    print("🔧 BẮT ĐẦU SỬA LỖI SLUGS...")
    print("=" * 50)
    
    news_items = News.objects.all()
    total_count = news_items.count()
    
    if total_count == 0:
        print("📝 Không có tin tức nào để sửa.")
        return
    
    print(f"📰 Tìm thấy {total_count} tin tức")
    fixed_count = 0
    
    for news in news_items:
        old_slug = news.slug
        
        # Generate new ASCII slug
        new_slug = vietnamese_slugify(news.title)
        
        # Ensure unique slug
        original_slug = new_slug
        counter = 1
        while News.objects.filter(slug=new_slug).exclude(pk=news.pk).exists():
            new_slug = f"{original_slug}-{counter}"
            counter += 1
        
        if old_slug != new_slug:
            news.slug = new_slug
            news.save(update_fields=['slug'])
            print(f"✅ '{news.title[:50]}...'")
            print(f"   Cũ: {old_slug}")
            print(f"   Mới: {new_slug}")
            print()
            fixed_count += 1
        else:
            print(f"⏭️  '{news.title[:50]}...' - slug đã OK")
    
    print("=" * 50)
    print(f"🎉 HOÀN THÀNH!")
    print(f"📊 Đã sửa: {fixed_count}/{total_count} tin tức")
    
    if fixed_count > 0:
        print("\n💡 BÂY GIỜ BẠN CÓ THỂ:")
        print("   1. Khởi động lại server Django")
        print("   2. Truy cập /tin-tuc/ để kiểm tra")
        print("   3. Các URL sẽ hoạt động bình thường")

if __name__ == "__main__":
    try:
        fix_news_slugs()
    except Exception as e:
        print(f"❌ LỖI: {e}")
        print("\n💡 CÁCH KHẮC PHỤC:")
        print("1. Đảm bảo bạn đang ở thư mục chính của project")
        print("2. Chạy: python manage.py shell")
        print("3. Import và chạy function fix_news_slugs() thủ công")
