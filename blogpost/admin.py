from django.contrib import admin
from .models import Category, Post


class postAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content",
        "is_deleted",
    ]

    list_display_links = [
        "title",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]


admin.site.register(Post, postAdmin)
admin.site.register(Category, CategoryAdmin)
