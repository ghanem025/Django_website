# Generated by Django 3.2.7 on 2021-09-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100000),
        ),
        migrations.AlterField(
            model_name='store',
            name='num_employees',
            field=models.DecimalField(decimal_places=0, max_digits=10000),
        ),
    ]
