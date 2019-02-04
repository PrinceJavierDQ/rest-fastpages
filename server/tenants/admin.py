from django.contrib import admin
from django.db import connection

from .models import Client


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial', 'created_at', 'updated_at')
    list_filter = ['paid_until']

    def get_queryset(self, request):
        qs = super(ClientAdmin, self).get_queryset(self)
        #  if connection.schema_name == 'public' and request.user.is_superuser:
        return qs
        #  return qs.filter(id__in=[connection.get_tenant().id])


# Register the admin class with the associated model


admin.site.register(Client, ClientAdmin)


