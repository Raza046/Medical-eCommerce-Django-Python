# Generated by Django 2.2.4 on 2020-02-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0019_auto_20200210_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='items',
            field=models.ManyToManyField(null=True, to='carts.CartItems'),
        ),
    ]
