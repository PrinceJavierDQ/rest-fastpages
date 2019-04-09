from django import forms
from django.contrib import admin
from tenant_users.permissions.models import UserTenantPermissions
from django.contrib.auth import admin as auth_admin
from .models import TenantUser
from .forms import UserChangeForm, UserCreationForm

# Register your models here.


class TenantUserAdmin(admin.ModelAdmin):

    list_display = ('email', 'first_name', 'last_name','is_active','is_verified','last_login',)
    list_filter = ('is_active', 'is_verified', 'last_login',)
    search_fields = ('email', 'first_name', 'last_name',)
    readonly_fields = ('last_login',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'tenants') }),
         ('Personal Info', {'fields': ('first_name', 'last_name') }),
         ('Status', {'fields': ('is_active', 'is_verified', 'last_login') })
         )


@admin.register(UserTenantPermissions)
class UserTenantPermissionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(TenantUser, TenantUserAdmin)
