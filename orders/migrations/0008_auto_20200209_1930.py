# Generated by Django 2.2.4 on 2020-02-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200209_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('NZ', 'New Zealand'), ('P', 'Pakistan'), ('U', 'USA'), ('A', 'Australia'), ('D', 'Dubai'), ('T', 'Turkey')], max_length=100, null=True),
        ),
    ]
