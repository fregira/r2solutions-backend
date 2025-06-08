from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'service_interest', 'member_since', 'is_active']
    list_filter = ['service_interest', 'is_active', 'member_since']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    readonly_fields = ['member_since']