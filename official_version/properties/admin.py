from django.contrib import admin
from .models import PropertyType, Property, PropertyImage, PropertyFeature, PropertyFeatureRelation


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


class PropertyFeatureRelationInline(admin.TabularInline):
    model = PropertyFeatureRelation
    extra = 1


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'price', 'area', 'district', 'city', 'status', 'featured', 'created_at']
    list_filter = ['property_type', 'status', 'featured', 'city', 'district']
    search_fields = ['title', 'address', 'description']
    list_editable = ['featured', 'status']
    inlines = [PropertyImageInline, PropertyFeatureRelationInline]
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'description', 'property_type', 'status', 'featured')
        }),
        ('Thông tin giá và diện tích', {
            'fields': ('price', 'area', 'bedrooms', 'bathrooms')
        }),
        ('Địa chỉ', {
            'fields': ('address', 'ward', 'district', 'city')
        }),
        ('Tọa độ', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'caption', 'is_primary']
    list_filter = ['is_primary', 'property__property_type']
    search_fields = ['property__title', 'caption']


@admin.register(PropertyFeature)
class PropertyFeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']
