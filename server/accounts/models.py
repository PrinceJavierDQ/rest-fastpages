from django.db import models
from tenant_users.tenants.models import UserProfile


class TenantUser(UserProfile):
    first_name = models.CharField("First Name", max_length=100, blank=True)
    last_name = models.CharField("Last Name", max_length=100, blank=True)

