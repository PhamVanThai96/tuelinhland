from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os


class PropertyType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Loại hình bất động sản")
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Loại hình bất động sản"
        verbose_name_plural = "Loại hình bất động sản"
    
    def __str__(self):
        return self.name


class Property(models.Model):
    PROPERTY_STATUS = [
        ('available', 'Có sẵn'),
        ('sold', 'Đã bán'),
        ('reserved', 'Đã đặt cọc'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    description = models.TextField(verbose_name="Mô tả")
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name="Loại hình")
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="Giá")
    area = models.FloatField(verbose_name="Diện tích (m²)")
    bedrooms = models.IntegerField(verbose_name="Số phòng ngủ", default=0)
    bathrooms = models.IntegerField(verbose_name="Số phòng tắm", default=0)
    
    # Location
    address = models.CharField(max_length=300, verbose_name="Địa chỉ")
    ward = models.CharField(max_length=100, verbose_name="Phường/Xã")
    district = models.CharField(max_length=100, verbose_name="Quận/Huyện")
    city = models.CharField(max_length=100, verbose_name="Tỉnh/Thành phố")
    
    # Status
    status = models.CharField(max_length=20, choices=PROPERTY_STATUS, default='available', verbose_name="Trạng thái")
    featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    
    # SEO
    latitude = models.FloatField(null=True, blank=True, verbose_name="Vĩ độ")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Kinh độ")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Bất động sản"
        verbose_name_plural = "Bất động sản"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def get_primary_image_url(self):
        """Return primary image URL or default placeholder"""
        # Get primary image
        primary_image = self.images.filter(is_primary=True).first()
        if primary_image and primary_image.image:
            try:
                # Check if file actually exists
                if hasattr(primary_image.image, 'url'):
                    url = primary_image.image.url
                    # Additional validation for file existence
                    if hasattr(primary_image.image, 'path'):
                        if os.path.exists(primary_image.image.path):
                            return url
                    else:
                        # For remote storage, trust the URL
                        return url
            except (ValueError, AttributeError, OSError) as e:
                print(f"Error accessing primary image: {e}")
        
        # Get first image if no primary
        first_image = self.images.first()
        if first_image and first_image.image:
            try:
                if hasattr(first_image.image, 'url'):
                    url = first_image.image.url
                    if hasattr(first_image.image, 'path'):
                        if os.path.exists(first_image.image.path):
                            return url
                    else:
                        return url
            except (ValueError, AttributeError, OSError) as e:
                print(f"Error accessing first image: {e}")
        
        # Return default placeholder
        return f"{settings.STATIC_URL}images/property-placeholder.svg"
    
    @property
    def formatted_area(self):
        """Format area in square meters"""
        return f"{self.area:.2f} m²"

    @property
    def formatted_price(self):
        """Format price in Vietnamese style"""
        if self.price >= 1000000000:  # >= 1 tỷ
            return f"{self.price/1000000000:.1f} tỷ"
        elif self.price >= 1000000:  # >= 1 triệu
            return f"{self.price/1000000:.0f} triệu"
        else:
            return f"{self.price:,.0f} VND"
    
    @property
    def get_full_address(self):
        """Get formatted full address"""
        address_parts = []
        if self.address:
            address_parts.append(self.address)
        if self.ward:
            address_parts.append(self.ward)
        if self.district:
            address_parts.append(self.district)
        if self.city:
            address_parts.append(self.city)
        return ", ".join(address_parts)
    
    @property
    def is_available(self):
        """Check if property is available"""
        return self.status == 'available'


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/', verbose_name="Hình ảnh")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Chú thích")
    is_primary = models.BooleanField(default=False, verbose_name="Ảnh chính")
    
    class Meta:
        verbose_name = "Hình ảnh bất động sản"
        verbose_name_plural = "Hình ảnh bất động sản"
    
    def __str__(self):
        return f"{self.property.title} - {self.caption}"
    
    def get_image_url_safe(self):
        """Return image URL or default placeholder"""
        if self.image:
            try:
                # Check if file actually exists
                if hasattr(self.image, 'url'):
                    url = self.image.url
                    if hasattr(self.image, 'path'):
                        if os.path.exists(self.image.path):
                            return url
                    else:
                        # For remote storage, trust the URL
                        return url
            except (ValueError, AttributeError, OSError) as e:
                print(f"Error accessing image: {e}")
        
        # Return default placeholder
        return f"{settings.STATIC_URL}images/property-placeholder.svg"


class PropertyFeature(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên tiện ích")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Icon class")
    
    class Meta:
        verbose_name = "Tiện ích"
        verbose_name_plural = "Tiện ích"
    
    def __str__(self):
        return self.name


class PropertyFeatureRelation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature = models.ForeignKey(PropertyFeature, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('property', 'feature')
        verbose_name = "Tiện ích bất động sản"
        verbose_name_plural = "Tiện ích bất động sản"
