from rest_framework import serializers
from server.tenants.models import Client
from server.accounts.models import TenantUser


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'paid_until', 'on_trial', 'owner')


class TenantUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TenantUser
        fields = ('id', 'first_name', 'last_name')


