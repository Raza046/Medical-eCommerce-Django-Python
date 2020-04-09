# Generated by Django 2.2.4 on 2020-02-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200210_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('NZ', 'New Zealand'), ('A', 'Australia'), ('D', 'Dubai'), ('T', 'Turkey'), ('P', 'Pakistan'), ('U', 'USA')], max_length=100, null=True),
        ),
    ]
