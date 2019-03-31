from .models import Page
from rest_framework import serializers


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('title', 'slug', 'status')
