# Generated by Django 3.2.7 on 2021-09-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_auto_20210926_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]
