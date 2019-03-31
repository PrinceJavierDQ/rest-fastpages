from django.contrib import admin
from .models import TenantUser
from tenant_users.permissions.models import UserTenantPermissions

# Register your models here.


class TenantUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_verified', 'last_login')
    list_filter = ['is_active', 'is_verified']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        # ('Permissions', {'fields': ('is_superuser',)}),
        ('Tenants', {'fields': ('tenants',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(UserTenantPermissions)
class UserTenantPermissionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(TenantUser, TenantUserAdmin)
