from rest_framework import serializers
from server.tenants.models import Client
from server.accounts.models import TenantUser
from server.pages.models import Page, ProductVariantOption


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'paid_until', 'on_trial', 'owner', 'domain_url')


class TenantUserSerializer(serializers.ModelSerializer):
    tenants = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = TenantUser
        fields = ('id', 'email', 'first_name', 'last_name', 'tenants')


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantOption
        fields = ('id', 'variant_name', 'variant_value')


class PageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'status', 'available_on', 'available_off',
                  'product_name', 'product_price', 'product_discount_price',
                  'product_image1', 'product_image2', 'product_image3', 'product_variant_options')


class PageSerializer(serializers.ModelSerializer):

    product_image1 = serializers.ImageField(max_length=None, use_url=True)
    product_image2 = serializers.ImageField(max_length=None, use_url=True)
    product_image3 = serializers.ImageField(max_length=None, use_url=True)
    product_image4 = serializers.ImageField(max_length=None, use_url=True)
    product_image5 = serializers.ImageField(max_length=None, use_url=True)
    product_image6 = serializers.ImageField(max_length=None, use_url=True)

    product_variant_options = ProductOptionSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'
        create_only_fields = ('title', 'slug', 'status', 'available_on', 'available_off')

