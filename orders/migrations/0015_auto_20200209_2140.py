# Generated by Django 2.2.4 on 2020-02-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200209_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('A', 'Australia'), ('NZ', 'New Zealand'), ('D', 'Dubai'), ('P', 'Pakistan'), ('T', 'Turkey'), ('U', 'USA')], max_length=100, null=True),
        ),
    ]
