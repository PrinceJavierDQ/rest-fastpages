from rest_framework import viewsets
from . import serializers
from server.tenants.models import Client
from server.accounts.models import TenantUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.TenantUserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer

