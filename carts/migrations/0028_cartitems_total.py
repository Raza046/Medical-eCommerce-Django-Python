# Generated by Django 2.2.4 on 2020-02-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0027_remove_cartitems_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
