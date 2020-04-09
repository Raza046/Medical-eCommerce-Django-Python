# Generated by Django 2.2.4 on 2020-01-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200126_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='subtotal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
