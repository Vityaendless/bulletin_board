from django.contrib import admin
from .models import Ad, Comment, Category


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['author', 'category', 'price', 'status']
    search_fields = ['title', 'description']
    fields = [
        'photo', 'title', 'description', 'author', 'category', 'price',
        'status', 'created_at', 'published_at', 'updated_at'
    ]
    readonly_fields = ['created_at', 'published_at', 'updated_at']


admin.site.register(Comment)

admin.site.register(Category)
