# Generated by Django 2.2.4 on 2020-02-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20200210_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('P', 'Pakistan'), ('U', 'USA'), ('NZ', 'New Zealand'), ('A', 'Australia'), ('D', 'Dubai'), ('T', 'Turkey')], max_length=100, null=True),
        ),
    ]
