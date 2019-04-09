import os
import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save


def upload_helper(instance, filename):
    ext = filename.rsplit(u'.', 1)[1]
    name = u'%s.%s' % (uuid.uuid1().hex[:8], ext)
    model_name = (instance.__class__.__name__).lower()
    return os.path.join(u'uploads', model_name, name)


class Page(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=20)
    status = models.BooleanField(default=True)
    available_on = models.DateField(null=True, blank=True)
    available_off = models.DateField(null=True, blank=True)
    hit_count = models.IntegerField(default=0)
    product_name = models.CharField(null=True, max_length=200)
    product_price = models.DecimalField(default=0, decimal_places=3, max_digits=8)
    product_discount_price = models.DecimalField(default=0, decimal_places=3, max_digits=8)
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

    class Meta:
        ordering = ["-available_on"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
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
