from django.contrib import admin

from .models import AppUser


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone']
    list_display_links = ['id', 'username', 'email']
    list_filter = ['id', 'username', 'email', 'phone']
    search_fields = ['username', 'email', 'phone']
    fields = [
        'username', 'avatar', 'password', 'email', 'first_name',
        'last_name', 'phone', 'ads_count', 'comments_count'
    ]
