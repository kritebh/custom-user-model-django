from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account 
# Register your models here.

class UserAdminConfig(UserAdmin):
    list_display=['email','username','first_name','date_of_birth','city']
    search_fields=['email','username','city']
    readonly_fields=['date_joined','last_login']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','first_name','last_name','date_of_birth','city')}),
        ('Activity', {'fields': ('date_joined','last_login')}),
        ('Permissions', {'fields': ('is_admin','is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name', 'date_of_birth','city', 'password1', 'password2'),
        }),
    )

admin.site.register(Account,UserAdminConfig)