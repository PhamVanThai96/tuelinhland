from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    project_type = models.CharField(max_length=50, choices=[
        ('LAND', 'Dự án đất nền'),
        ('APARTMENT', 'Dự án chung cư'),
        ('VILLA', 'Dự án biệt thự'),
        ('SHOPHOUSE', 'Shophouse'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
