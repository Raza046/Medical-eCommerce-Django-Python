# Generated by Django 2.2.4 on 2020-02-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_quantity'),
        ('carts', '0016_cartitems_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='prod',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='prod',
            field=models.ManyToManyField(null=True, to='products.Products'),
        ),
    ]
