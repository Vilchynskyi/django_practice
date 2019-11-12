from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    readonly_fields = ('date_of_publ',)


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('post',)
    list_display_links = ('post',)
