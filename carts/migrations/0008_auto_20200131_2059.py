# Generated by Django 2.2.4 on 2020-01-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_auto_20200131_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
