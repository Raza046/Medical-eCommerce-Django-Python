# Generated by Django 2.2.4 on 2020-01-31 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20200126_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='quantity',
        ),
    ]
