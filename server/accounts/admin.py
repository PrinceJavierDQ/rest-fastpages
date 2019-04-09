from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from tenant_users.permissions.models import UserTenantPermissions
from .models import TenantUser

# Register your models here.


class TenantUserAdmin(BaseAdmin):

    list_display = ('email', 'first_name', 'last_name','is_active','is_verified','last_login',)
    list_filter = ('is_active', 'is_verified', 'last_login',)
    search_fields = ('email', 'first_name', 'last_name',)
    readonly_fields = ('last_login',)
    filter_horizontal = ()
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'tenants')}),
         ('Personal Info', {'fields': ('first_name', 'last_name')}),
         ('Status', {'fields': ('is_active', 'is_verified', 'last_login')})
         )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'tenants') }),
         ('Personal Info', {'fields': ('first_name', 'last_name') }),
         ('Status', {'fields': ('is_active', 'is_verified')})
         )

    # def get_form(self, request, obj=None, **kwargs):
    #    # Proper kwargs are form, fields, exclude, formfield_callback
    #   if obj is None:
    #        self.form = UserAdminCreationForm
    #    else:
    #        self.form = UserAdminChangeForm
    #    return super(TenantUserAdmin, self).get_form(request, obj, **kwargs)


@admin.register(UserTenantPermissions)
class UserTenantPermissionsAdmin(admin.ModelAdmin):
    list_display = ('profile', 'is_staff', 'is_superuser')



admin.site.register(TenantUser, TenantUserAdmin)
