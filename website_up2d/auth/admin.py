from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    # untuk di tampilin di django admin kolomnya
    list_display = (
        'id', 'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_admin', 'is_participant'
        )
    # untuk menampilkan field untuk melihat detail dari user
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_admin', 'is_participant')
        })
    )
    # untuk mengampilkan file apa saja yang ditampilkan kalau mau menambah user baru di django admin
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_admin', 'is_participant')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)