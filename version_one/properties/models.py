from django.db import models
from django.contrib.auth.models import User


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
