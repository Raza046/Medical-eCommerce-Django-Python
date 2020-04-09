# Generated by Django 2.2.4 on 2020-01-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200131_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('A', 'Australia'), ('NZ', 'New Zealand'), ('T', 'Turkey'), ('P', 'Pakistan'), ('D', 'Dubai'), ('U', 'USA')], max_length=100, null=True),
        ),
    ]
