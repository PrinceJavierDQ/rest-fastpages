import os
import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from server.accounts.models import TenantUser


def upload_helper(instance, filename):
    ext = filename.rsplit(u'.', 1)[1]
    name = u'%s.%s' % (uuid.uuid1().hex[:8], ext)
    model_name = (instance.__class__.__name__).lower()
    instance_id = instance.id
    return os.path.join(u'uploads', model_name, str(instance_id), name)


def my_random_slug():
    return get_random_string(length=20)


class Page(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, default=my_random_slug, unique=True, max_length=20)
    status = models.BooleanField(default=True)
    available_on = models.DateField(null=True, blank=True)
    available_off = models.DateField(null=True, blank=True)
    hit_count = models.IntegerField(default=0)
    product_name = models.CharField(null=True, max_length=200)
    product_price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    product_discount_price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    product_discount_until = models.DateTimeField(null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_details = models.TextField(null=True, blank=True)
    product_size_image = models.ImageField(upload_to=upload_helper, null=True)
    product_image1 = models.ImageField(upload_to=upload_helper, null=True)
    product_image2 = models.ImageField(upload_to=upload_helper, null=True)
    product_image3 = models.ImageField(upload_to=upload_helper, null=True)
    product_image4 = models.ImageField(upload_to=upload_helper, null=True)
    product_image5 = models.ImageField(upload_to=upload_helper, null=True)
    product_image6 = models.ImageField(upload_to=upload_helper, null=True)
    product_showcase1 = models.ImageField(upload_to=upload_helper, null=True)
    product_showcase2 = models.ImageField(upload_to=upload_helper,null=True)
    product_showcase3 = models.ImageField(upload_to=upload_helper,null=True)
    product_showcase4 = models.FileField(upload_to=upload_helper, null=True, verbose_name="")
    owner = models.ForeignKey(TenantUser, related_name='owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updater = models.ForeignKey(TenantUser, related_name='updater', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-available_on"]


class ProductVariantOption(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='product_variant_options')
    variant_name = models.CharField(max_length=100) # Size or Colour
    variant_value = models.CharField(max_length=100) # S (Size) or Red (Colour)

    class Meta:
        unique_together = (('page', 'variant_name', 'variant_value'),)


class ProductVariant(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)


# Product Variant
#   Colour = Red, Size = Small


class ProductVariantDetail(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    variant_option = models.ForeignKey(ProductVariantOption, on_delete=models.CASCADE)


class Order(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    sub_district = models.CharField(max_length=100, help_text="ตำบล")
    district = models.CharField(max_length=100, help_text="อำเภอ")
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    order_date = models.DateField(blank=True, null=True)
    order_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(default=0, decimal_places=2, max_digits=8)


def create_slug(instance, new_slug=None):
    # slug = slugify(instance.title)
    slug = get_random_string(length=20)
    if new_slug is not None:
        slug = new_slug
    qs = Page.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s:%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance,)


pre_save.connect(pre_save_post_receiver, sender=Page)
