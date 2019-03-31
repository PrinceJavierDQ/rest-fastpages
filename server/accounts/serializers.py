from .models import TenantUser
from rest_framework import serializers


class TenantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TenantUser
        fields = ('pk', 'email', 'first_name', 'last_name', 'tenants')
        read_only_fields = ('email', 'tenants',)

