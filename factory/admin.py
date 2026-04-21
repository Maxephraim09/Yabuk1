from django.contrib import admin

from .models import BlogPost, ContactMessage, SiteImage, SiteSnippet


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")


@admin.register(SiteSnippet)
class SiteSnippetAdmin(admin.ModelAdmin):
    list_display = ("group", "label", "is_active", "sort_order", "updated_at")
    list_filter = ("group", "is_active")
    search_fields = ("key", "label", "value")


@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ("group", "label", "is_active", "sort_order", "updated_at")
    list_filter = ("group", "is_active")
    search_fields = ("key", "label", "alt_text")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "sort_order", "published_at")
    list_filter = ("is_published", "category")
    search_fields = ("title", "category", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
