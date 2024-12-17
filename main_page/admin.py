from django.contrib import admin

# Register your models here.
# articles/admin.py
from django.contrib import admin
from .models import main_page

@admin.register(main_page)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)