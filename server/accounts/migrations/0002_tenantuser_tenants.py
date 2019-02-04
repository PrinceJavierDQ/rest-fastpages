# Generated by Django 2.1.4 on 2018-12-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantuser',
            name='tenants',
            field=models.ManyToManyField(blank=True, help_text='The tenants this user belongs to.', related_name='user_set', to='tenants.Client', verbose_name='tenants'),
        ),
    ]
