# Generated by Django 2.2.4 on 2020-02-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0030_auto_20200210_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
