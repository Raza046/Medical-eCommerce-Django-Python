# Generated by Django 2.2 on 2020-04-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_auto_20200214_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('NZ', 'New Zealand'), ('T', 'Turkey'), ('D', 'Dubai'), ('P', 'Pakistan'), ('A', 'Australia'), ('U', 'USA')], max_length=100, null=True),
        ),
    ]
