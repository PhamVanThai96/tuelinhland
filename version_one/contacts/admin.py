from django.contrib import admin
from .models import Contact, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["name", "phone", "email"]
    list_editable = ["status"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Thông tin liên hệ", {"fields": ("name", "phone", "email", "message")}),
        ("Trạng thái", {"fields": ("status",)}),
        (
            "Thời gian",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email", "subscribed_at", "is_active"]
    list_filter = ["is_active", "subscribed_at"]
    search_fields = ["email"]
    list_editable = ["is_active"]
    readonly_fields = ["subscribed_at"]
