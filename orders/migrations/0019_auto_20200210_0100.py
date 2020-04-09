# Generated by Django 2.2.4 on 2020-02-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200210_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('D', 'Dubai'), ('A', 'Australia'), ('T', 'Turkey'), ('P', 'Pakistan'), ('NZ', 'New Zealand'), ('U', 'USA')], max_length=100, null=True),
        ),
    ]
