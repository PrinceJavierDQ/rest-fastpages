from .models import Client
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('domain_url', 'schema_name', 'name', 'paid_until', 'on_trial', 'owner')

