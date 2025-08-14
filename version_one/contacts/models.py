from django.db import models


class Contact(models.Model):
    CONTACT_STATUS = [
        ("new", "Mới"),
        ("contacted", "Đã liên hệ"),
        ("completed", "Hoàn thành"),
    ]

    name = models.CharField(max_length=100, verbose_name="Họ và tên")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, verbose_name="Email")
    message = models.TextField(blank=True, verbose_name="Tin nhắn")
    status = models.CharField(
        max_length=20, choices=CONTACT_STATUS, default="new", verbose_name="Trạng thái"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        verbose_name = "Liên hệ"
        verbose_name_plural = "Liên hệ"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đăng ký")
    is_active = models.BooleanField(default=True, verbose_name="Đang hoạt động")

    class Meta:
        verbose_name = "Đăng ký nhận tin"
        verbose_name_plural = "Đăng ký nhận tin"
        ordering = ["-subscribed_at"]

    def __str__(self):
        return self.email
