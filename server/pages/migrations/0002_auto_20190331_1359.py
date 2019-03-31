# Generated by Django 2.1.7 on 2019-03-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='product_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='product_discount_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='page',
            name='product_image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_image4',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='product_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='page',
            name='product_showcase1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_showcase2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_showcase3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_showcase4',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
