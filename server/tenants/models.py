from django.db import models
from server.accounts.models import TenantUser
# from tenant_schemas.models import TenantMixin
from tenant_users.tenants.models import TenantBase
from datetime import datetime, timedelta
from django.utils import timezone
# Create your models here.


class Client(TenantBase):
    name = models.CharField(max_length=200)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.OneToOneField(TenantUser, related_name='client_created_by', on_delete=models.CASCADE)
    owner = models.OneToOneField(TenantUser, related_name='client_owner', on_delete=models.CASCADE)
    # updated_by = models.OneToOneField(TenantUser, related_name='client_updated_by', on_delete=models.CASCADE)
    auto_create_schema = True

    def save(self, *args, **kwargs):
        if not self.paid_until:
            self.paid_until = timezone.datetime.today() + timedelta(days=30)
        self.last_modified = timezone.now()
        return super(Client, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = 'paid_until'

    def __str__(self):
        return self.name

