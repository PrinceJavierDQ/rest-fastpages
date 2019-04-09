from django import forms
from django.contrib import admin
from tenant_users.permissions.models import UserTenantPermissions
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

    def get_form(self, request, obj=None, **kwargs):
        # Proper kwargs are form, fields, exclude, formfield_callback
        if obj is None:
            self.form = UserCreationForm
        else:
            self.form = UserChangeForm
        return super(TenantUserAdmin, self).get_form(request, obj, **kwargs)


@admin.register(UserTenantPermissions)
class UserTenantPermissionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(TenantUser, TenantUserAdmin)
