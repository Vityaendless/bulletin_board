from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUser


@admin.register(AppUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'phone']
    list_display_links = ['id', 'username', 'email']
    list_filter = ['id', 'username', 'email', 'phone']
    search_fields = ['username', 'email', 'phone']
