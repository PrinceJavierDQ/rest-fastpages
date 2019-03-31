from rest_framework import serializers
from server.tenants.models import Client
from server.accounts.models import TenantUser
from server.pages.models import Page


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'paid_until', 'on_trial', 'owner', 'domain_url')


class TenantUserSerializer(serializers.ModelSerializer):
    tenants = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = TenantUser
        fields = ('id', 'email', 'first_name', 'last_name', 'tenants')


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'status')
