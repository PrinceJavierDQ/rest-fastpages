from django.core.management.base import BaseCommand
from server.accounts.models import TenantUser
from server.settings.components import config
from django.contrib.auth import get_user_model

# from tenant_users.tenants.tasks import provision_tenant
from tenant_users.tenants.utils import create_public_tenant


class Command(BaseCommand):
    help = 'Create public tenant for the system'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('email', nargs='+', type=str)
        parser.add_argument('password', nargs='+', type=str)

    def handle(self, *args, **options):
        email = options['email'][0]
        password = options['password'][0]
        create_public_tenant(config('DOMAIN_NAME'), email)
        UserModel = get_user_model()
        user = UserModel.objects.filter(email=email).first()
        if user:
            user.set_password(password)
            user.save()
