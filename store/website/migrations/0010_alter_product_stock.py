# Generated by Django 3.2.8 on 2021-10-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1000000),
        ),
    ]
