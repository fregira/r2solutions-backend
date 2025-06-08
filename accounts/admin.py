from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'service_interest', 'created_at',
                    'is_active']
    list_filter = ['service_interest', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'phone')
        }),
        ('Service info', {
            'fields': ('service_interest',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'created_at', 'updated_at'),
        }),
    )