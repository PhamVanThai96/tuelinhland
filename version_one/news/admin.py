from django.contrib import admin
from django.utils.html import format_html
from .models import Category, News, NewsTag, NewsTagRelation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class NewsTagInline(admin.TabularInline):
    model = NewsTagRelation
    extra = 1

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'status', 'is_featured', 'views_count', 'published_at']
    list_filter = ['status', 'category', 'is_featured', 'created_at']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views_count', 'created_at', 'updated_at']
    inlines = [NewsTagInline]
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Phân loại', {
            'fields': ('category', 'author', 'status', 'is_featured')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Thống kê', {
            'fields': ('views_count', 'created_at', 'updated_at', 'published_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'author')
