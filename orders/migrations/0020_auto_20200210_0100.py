# Generated by Django 2.2.4 on 2020-02-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20200210_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('P', 'Pakistan'), ('A', 'Australia'), ('D', 'Dubai'), ('T', 'Turkey'), ('U', 'USA'), ('NZ', 'New Zealand')], max_length=100, null=True),
        ),
    ]
