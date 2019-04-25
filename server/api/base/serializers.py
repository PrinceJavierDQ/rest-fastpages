from rest_framework import serializers
from rest_framework.response import Response

from server.tenants.models import Client
from server.accounts.models import TenantUser
from server.pages.models import Page, ProductVariantOption


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'paid_until', 'on_trial', 'owner', 'domain_url')


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


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

    product_variant_options = ProductOptionSerializer(many=True)

    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'status', 'available_on', 'available_off',
                  'product_name', 'product_price', 'product_discount_price', 'product_discount_until',
                  'product_image1', 'product_image2', 'product_image3',
                  'product_image4', 'product_image5', 'product_image6',
                  'product_showcase1', 'product_showcase2', 'product_showcase3',
                  'product_variant_options', 'product_details')

    def update(self, instance, validated_data):
        variant_options = validated_data.pop('product_variant_options')

        pid = Page.objects.filter(pk=instance.id).update(**validated_data)
        instance = Page.objects.filter(pk=pid).first()
        keep_options = []
        # existing_ids = [o.id for o in instance.product_variant_options]
        for variant_option in variant_options.all():
            if "id" in variant_option.keys():  # existing record
                if ProductVariantOption.objects.filter(id=variant_options["id"]).exists():
                    # this record may need update
                    option = ProductVariantOption.objects.get(id=variant_options["id"])
                    option.variant_name = variant_option.get('variant_name', option.variant_name)
                    option.variant_value = variant_option.get('variant_value', option.variant_value)
                    option.save()
                    keep_options.append(option.id)
                # else:
                    # option = ProductVariantOption.objects.create(page=instance, **variant_option)
                    # keep_options.append(option.id)
            else:
                option = ProductVariantOption.objects.create(page=instance, **variant_option)
                keep_options.append(option.id)

        for variant_option in instance.product_variant_options.all():
            if variant_option.id not in keep_options:
                variant_option.delete()

        return instance


class PageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'status', 'available_on', 'available_off')


class PageSerializer(serializers.ModelSerializer):

    product_image1 = serializers.ImageField(max_length=None, use_url=True)
    product_image2 = serializers.ImageField(max_length=None, use_url=True)
    product_image3 = serializers.ImageField(max_length=None, use_url=True)
    product_image4 = serializers.ImageField(max_length=None, use_url=True)
    product_image5 = serializers.ImageField(max_length=None, use_url=True)
    product_image6 = serializers.ImageField(max_length=None, use_url=True)

    product_showcase1 = serializers.ImageField(max_length=None, use_url=True)
    product_showcase2 = serializers.ImageField(max_length=None, use_url=True)
    product_showcase3 = serializers.ImageField(max_length=None, use_url=True)
    product_showcase4 = serializers.ImageField(max_length=None, use_url=True)

    product_variant_options = ProductOptionSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'
        create_only_fields = ('title', 'slug', 'status', 'available_on', 'available_off')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = '__all__'
