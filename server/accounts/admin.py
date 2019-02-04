from django.contrib import admin
from .models import TenantUser

# Register your models here.


class TenantUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_verified', 'last_login')
    list_filter = ['is_active', 'is_verified']


admin.site.register(TenantUser, TenantUserAdmin)
