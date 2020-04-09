# Generated by Django 2.2.4 on 2020-02-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20200210_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('NZ', 'New Zealand'), ('U', 'USA'), ('A', 'Australia'), ('T', 'Turkey'), ('D', 'Dubai'), ('P', 'Pakistan')], max_length=100, null=True),
        ),
    ]
